/**
 * 2021/05/23
 * Binary Tree Level Order Traversal II: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
 * Basically,  just reverse the result of #102
 */
 class Solution {
    fun levelOrderBottom(root: TreeNode?): List<List<Int>> {
        val resultList: MutableList<List<Int>> = mutableListOf<List<Int>>()
        root?.let { rootNode ->
            val levelList: MutableList<List<TreeNode>> = mutableListOf<List<TreeNode>>(listOf(rootNode))
            while(!levelList.isEmpty()) {
                val currentLevelList = levelList[0]
                val currentValList = mutableListOf<Int>()
                val nextLevelList = mutableListOf<TreeNode>()
                currentLevelList.forEach { node ->
                    currentValList.add(node.`val`)
                    node.left?.let {
                        nextLevelList.add(it)
                    }
                    node.right?.let {
                        nextLevelList.add(it)
                    }
                }
                if(!currentLevelList.isEmpty()) {
                    resultList.add(0,currentValList)
                }
                if(!nextLevelList.isEmpty()) {
                    levelList.add(nextLevelList)
                }
                levelList.removeAt(0)
            }
        }
        return resultList
    }
}
