##https://leetcode.com/problems/counting-bits/
class Solution(object):
    def countBits(self,num):
        res = [0 for i in range (num+1)]
        print "res",res
        if num == 0:
            return res
        if num == 1:
            res[num] = 1
            return res
        i = 1
        rest =  num + 1
        res[1]=1
        print "res[1]", res
        while rest >= 2**i:
            rest = rest - 2**i
            print "rest", rest
            i = i + 1
            print "i in loop", i
        print "i", i
        j = 1
        position = 2
        while j <= i:
            while position > 2**j - 1 and position < 2**(j+1)and position <= num:
                print "position", position
                res[position]=res[position-2**j]+1
                position += 1
            j += 1
            print "j in loop", j
        return res
test = Solution()
print test.countBits(8)


            
        
        
        
