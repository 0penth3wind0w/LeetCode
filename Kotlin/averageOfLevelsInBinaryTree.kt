/**
 * 2021/05/23
 * Average of Levels in Binary Tree: https://leetcode.com/problems/average-of-levels-in-binary-tree/
 */
 class Solution {
    fun averageOfLevels(root: TreeNode?): DoubleArray {
        val resultList = mutableListOf<Double>()
        root?.let { rootNode ->
            var levelList: List<TreeNode>? = listOf(rootNode)
            while(levelList != null) {
                var currentLevelSum = 0.0
                var currentLevelCount = 0.0
                val nextLevelList = mutableListOf<TreeNode>()
                levelList.forEach { node ->
                    currentLevelSum += node.`val`.toDouble()
                    currentLevelCount += 1.0
                    node.left?.let {
                        nextLevelList.add(it)
                    }
                    node.right?.let {
                        nextLevelList.add(it)
                    }
                }
                resultList.add(currentLevelSum.toDouble() / currentLevelCount)
                when(nextLevelList.isEmpty()) {
                    true -> levelList = null
                    false -> levelList = nextLevelList
                }
            }
        }
        return resultList.toDoubleArray()
    }
}
