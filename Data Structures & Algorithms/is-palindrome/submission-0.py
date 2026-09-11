class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" ", "")
        r = s[::-1]
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        r = re.sub(r'[^a-zA-Z0-9]', '', r)
        if s.lower() == r.lower():
            return True
        return False