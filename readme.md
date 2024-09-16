```python

    def factorial(n):
        Calculates the factorial of a given number n.\
            
        Args:
        n (int): The number to calculate the factorial of.
        
        Returns:
        int: The factorial of n.
        if n == 0:
            return 1    
        else:        
            return n * factorial(n-1)
        \n```\n\n**Example Usage:**\n\n```python\n>>> factorial(5)\n120\n>>> factorial(0)\n1\n```\n\n**Explanation:**\n\n* The function definition is `def factorial(n):`.\n* It takes one argument, `n`, which represents the number to calculate the factorial of.\n* The base case is when `n` is `0`, in which case the function returns `1` (since the factorial of 0 is 1).\n* For any positive `n`, it recursively calls itself with `n-1` as the argument and multiplies the result by `n`.\n* The recursion continues until the base case is reached, at which point the final result is returned.\n\n**Time Complexity:**\n\n* O(n), where n is the number being factored.\n\n**Space Complexity:**\n\n* O(1), as the function only requires a few variables to store temporary values during the recursion.\n\n**Note:**\n\n* This function can only handle non-negative integers as input.\n* For large numbers, the factorial calculation can take a long time or even exceed the available memory. In such cases, iterative approaches are recommended.