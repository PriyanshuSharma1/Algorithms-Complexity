class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        open_brac=["(","{","["]
        close_brac=[")","}","]"]
        for element in s:
            if element in open_brac:
                stack.append(element)
            else:
                if len(stack)==0:
                    return 0
                elif open_brac.index(stack[-1])==close_brac.index(element):
                    stack.pop()