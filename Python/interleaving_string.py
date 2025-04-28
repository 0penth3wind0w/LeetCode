class Solution:
    records = {}
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # return result if calculated
        rec = self.records.get(f"{s1},{s2},{s3}", None)
        if rec is not None :
            return rec
        ls1, ls2 = len(s1), len(s2)
        # ensure s1 is shorter
        if ls1 > ls2:
            return self.isInterleave(s2, s1, s3)
        # calculate result
        if ls1 + ls2 != len(s3): # obvious false case - 1
            self.records[f"{s1},{s2},{s3}"] = False
            return False
        # print(f"{s1},{s2},{s3}")
        if ls1 != 0:
            if s1[0] != s3[0] and s2[0] != s3[0]: # obvious false case - 2
                self.records[f"{s1},{s2},{s3}"] = False
                return False
            else:
                # divide problem to smaller subproblems
                r1 = self.isInterleave(s1[1:], s2, s3[1:]) if s1[0] == s3[0] else False
                # return the result, need no calculate other possibility
                if r1:
                    self.records[f"{s1},{s2},{s3}"] = True
                    return True
                r2 = self.isInterleave(s1, s2[1:], s3[1:]) if s2[0] == s3[0] else False
                self.records[f"{s1},{s2},{s3}"] = r2
                return r2
        # ls1 == 0
        self.records[f"{s1},{s2},{s3}"] = s2 == s3
        return s2 == s3
