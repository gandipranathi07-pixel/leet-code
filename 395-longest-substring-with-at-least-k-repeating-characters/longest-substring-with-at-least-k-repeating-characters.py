class Solution(object):
    def longestSubstring(self, s, k):

        unique = len(set(s))
        ans = 0

        for u in range(1, unique + 1):

            freq = {}
            left = 0
            count = 0
            unique_count = 0

            for right in range(len(s)):

                ch = s[right]

                if ch not in freq:
                    freq[ch] = 0

                freq[ch] += 1

                if freq[ch] == 1:
                    unique_count += 1

                if freq[ch] == k:
                    count += 1

                while unique_count > u:

                    ch = s[left]

                    if freq[ch] == k:
                        count -= 1

                    freq[ch] -= 1

                    if freq[ch] == 0:
                        unique_count -= 1

                    left += 1

                if unique_count == u and count == u:
                    ans = max(ans, right - left + 1)

        return ans   