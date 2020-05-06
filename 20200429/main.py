class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    index_left = 0
    index_right = 0 
    current_longest_distance = 0

    frequency = [0] * 26

    current_start = 0
    i = 0
    for c in s:
        frequency_idx = ord(c) - ord('a')
        frequency[frequency_idx] = frequency[frequency_idx] + 1
        if frequency[frequency_idx] > 1:
            if s[i - 1] == c:
                if i - 1 - current_start > current_longest_distance:
                    current_longest_distance = i - 1 - current_start
                    index_left = current_start
                    index_right = i - 1
                    current_start = i

                    for j in range(len(frequency)):
                        frequency[j] = 0        

        i = i + 1   
    
    return index_right - index_left + 1

print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10

# Looking back at this solution, it probably is not exactly what is requested