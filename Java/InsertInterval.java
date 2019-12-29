/**
 * 2019/12/08
 * Insert Interval: https://leetcode.com/problems/insert-interval/
 */

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int[] toInsert = newInterval;
        List<int[]> listResult = new ArrayList<int[]>();
        for (int i = 0; i<intervals.length; ++i) {
            //newInterval insert before 
            if (intervals[i][0] > toInsert[1]){
                listResult.add(toInsert);
                toInsert = intervals[i];
            }
            //new interval after
            else if ((toInsert[0] > intervals[i][1]))  {
                listResult.add(intervals[i]);
            }
            // overlap type 1 + identical
            else if (intervals[i][0] <= toInsert[0] && intervals[i][1] >= toInsert[1]) {
                toInsert = intervals[i];
            }
            // overlap type 2
            // else if (intervals[i][0] > toInsert[0] && intervals[i][1] < toInsert[1]) {
            //     // do nothing
            // }
            // // overlap type 3
            else if (intervals[i][0] <= toInsert[0] && intervals[i][1] <= toInsert[1]) {
                toInsert = new int[] {intervals[i][0], toInsert[1]};
            }
            // overlap type 4
            else if (intervals[i][0] > toInsert[0] && intervals[i][1] > toInsert[1]) {
                toInsert = new int[] {toInsert[0], intervals[i][1]};
            }
        }
        listResult.add(toInsert);
        return listResult.toArray(new int[listResult.size()][2]);
    }
}