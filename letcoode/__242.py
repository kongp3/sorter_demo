# -*- coding: utf-8 -*-
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False

        bucket_s = list()
        bucket_t = list()

        for i in range(0, 26):
            bucket_s.append(0)
            bucket_t.append(0)

        for i in range(0, len_s):
            bucket_s[ord(s[i]) - 97] += 1
            bucket_t[ord(t[i]) - 97] += 1

        if bucket_s == bucket_t:
            return True
        else:
            return False


if __name__ == '__main__':
    ob = Solution()
    print ob.isAnagram("anagram", "nagaram")

