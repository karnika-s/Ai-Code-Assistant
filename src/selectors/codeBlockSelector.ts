import * as vscode from 'vscode';

export class CodeBlockSelector {
    static async loadCustomCodeItems(chatProvider: any) {
        const activeEditor = vscode.window.activeTextEditor;
        if (activeEditor) {
            const document = activeEditor.document;
            const symbols = await vscode.commands.executeCommand<vscode.DocumentSymbol[]>(
                'vscode.executeDocumentSymbolProvider',
                document.uri
            );

            if (symbols) {
                const symbolNames = symbols.map(symbol => symbol.name);
                const selectedSymbol = await vscode.window.showQuickPick(symbolNames, {
                    placeHolder: 'Select a code item from the current file'
                });

                if (selectedSymbol) {
                    const selectedSymbolContent = symbols.find(symbol => symbol.name === selectedSymbol);
                    const customContext = document.getText(selectedSymbolContent?.range);
                    chatProvider.addContext(customContext);
                    vscode.window.showInformationMessage('Custom code context loaded.');
                }
            }
        }
    }
}
