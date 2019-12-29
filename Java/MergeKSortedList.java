/**
 * 2019/12/07
 * Merge k Sorted Lists: https://leetcode.com/problems/merge-k-sorted-lists/
 * 
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ArrayList<ListNode> alists = new ArrayList<ListNode>();
        Collections.addAll(alists, lists);
        ListNode result = null;
        ListNode last = null;
        while (true) {
            boolean empty = false;
            System.out.println(alists.size());
            ListNode min = new ListNode(Integer.MAX_VALUE);
            int mindex = -1;
            if ( alists.isEmpty() ) {
                break;
            }
            for ( int i=0; i<alists.size(); i++) {
                ListNode cur = alists.get(i);
                if ( cur == null) {
                    empty = true;
                    alists.remove(i);
                    break;
                }
                else if ( cur.val <= min.val) {
                    min = cur;
                    mindex = i;
                }
            }
            if ( !empty && mindex != -1 ) {
                if (result == null) {
                    result = min;
                    last = result;
                }
                else {
                    last.next = min;
                    last = min;
                }
                alists.set(mindex, last.next);
            }
        }
        return result;
    }
}