class Solution:
    def addBinary(self, a: str, b: str) -> str:
        an = []
        carry = 0
        k = len(a) - 1
        l = len(b) - 1
        while k >= 0 or l >= 0 or carry:
            if k >= 0:
                carry += int(a[k])
                k -= 1
            if l >= 0:
                carry += int(b[l])
                l -= 1
            an.append(str(carry % 2))
            carry //= 2
        return ''.join(reversed(an))