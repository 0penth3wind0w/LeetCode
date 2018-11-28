'''
    2018/11/28
    Valid Square: https://leetcode.com/problems/valid-square/
'''

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        result = True
        links = list()
        f_links = list()
        links.append(((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5)
        links.append(((p1[0]-p3[0])**2+(p1[1]-p3[1])**2)**0.5)
        links.append(((p1[0]-p4[0])**2+(p1[1]-p4[1])**2)**0.5)
        links.append(((p2[0]-p3[0])**2+(p2[1]-p3[1])**2)**0.5)
        links.append(((p2[0]-p4[0])**2+(p2[1]-p4[1])**2)**0.5)
        links.append(((p3[0]-p4[0])**2+(p3[1]-p4[1])**2)**0.5)
        if 0 in links:
            result = False
        else:
            f_links = list(set(links))
            result = True if len(f_links)==2 else False
        
        return result