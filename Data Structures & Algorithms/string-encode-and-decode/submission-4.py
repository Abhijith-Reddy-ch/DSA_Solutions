class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += s + "~"
        return ans

    def decode(self, s: str) -> List[str]:
        res = []
        curr = ""

        for ch in s:
            if ch == "~":
                res.append(curr)
                curr = ""
            else:
                curr += ch

        return res