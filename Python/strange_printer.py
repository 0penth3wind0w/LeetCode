'''
    2024/08/25
    Strange Printer: https://leetcode.com/problems/strange-printer/description/
'''

class Solution:
    record = {}
    def sPrinter(self, s: str) -> int:
        # print(f"{s=}")
        if not s:
            return 0
        if len(set(s)) == len(s):
            # print(f"{s}: {len(s)}")
            return len(s)
        s_record = self.record.get(s, None)
        if s_record is not None:
            # print(f"{s}: {s_record} (cached)")
            return s_record
        s_rev_record = self.record.get(s[::-1], None)
        if s_rev_record is not None:
            # print(f"{s}: {s_rev_record} (cached rev.)")
            return s_rev_record
        
        head_char = s[0]
        tail_char = s[-1]

        if head_char == tail_char:
            char_index = []
            for i, c in enumerate(s):
                if c == head_char and i != 0 and i != len(s) - 1:
                    char_index.append(i)
            result_split = [ float("inf"), self.sPrinter(s.strip(head_char)) + 1 ]
            result_split.extend([ self.sPrinter(s[0:i+1]) + self.sPrinter(s[i:]) - 1 for i in char_index ])
            self.record[s] = min(*result_split)
            return self.record[s]
        
        char_index_h = []
        char_index_t = []
        for i, c in enumerate(s):
            if c == head_char and i != 0:
                char_index_h.append(i)
            if c == tail_char and i != len(s) - 1:
                char_index_t.append(i)
        result_split_h = [ float("inf"), self.sPrinter(s.strip(head_char)) + 1]
        result_split_h.extend([ self.sPrinter(s[0:i+1]) + self.sPrinter(s[i+1:]) for i in char_index_h ])
        result_split_l = [ float("inf"), self.sPrinter(s.strip(tail_char)) + 1 ]
        result_split_l.extend([ self.sPrinter(s[0:i]) + self.sPrinter(s[i:]) for i in char_index_t ])

        self.record[s] = min(*result_split_h, *result_split_l)
        return self.record[s]

    def strangePrinter(self, s: str) -> int:
        pruned = s[0]    
        for c in s:
            if c != pruned[-1]:
                pruned += c
        return self.sPrinter(pruned)
