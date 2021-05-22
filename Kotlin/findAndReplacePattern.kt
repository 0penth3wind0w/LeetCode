/**
 * 2021/05/22
 * Find and Replace Pattern: https://leetcode.com/problems/find-and-replace-pattern/
 */
class Solution {
    fun findAndReplacePattern(words: Array<String>, pattern: String): List<String> {
        val result: ArrayList<String> = ArrayList()
        for( word in words) {
            val patternToWordMap = mutableMapOf<Char, Char>()
            val wordToPatternMap = mutableMapOf<Char, Char>()
            var ok = true
            for (n in 0..pattern.length-1) {
                if (ok) {
                    when(patternToWordMap[pattern[n]]) {
                        null -> patternToWordMap.put(pattern[n], word[n])
                        word[n] -> Unit
                        else -> {ok = false}
                    }
                    if (ok) {
                        when(wordToPatternMap[word[n]]) {
                            null -> wordToPatternMap.put(word[n], pattern[n])
                            pattern[n] -> Unit
                            else -> {ok = false}
                        }
                        if(ok && n == pattern.length-1) {
                            result.add(word)
                        }
                    }
                }
            }
        }
        return result
    }
}