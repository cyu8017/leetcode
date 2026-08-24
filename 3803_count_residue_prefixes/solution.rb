# LeetCode 3803 - Count Residue Prefixes
# https://leetcode.com/problems/count-residue-prefixes/

# @param {String} s
# @return {Integer}
def residue_prefixes(s)
  st = {}
  ans = 0
  s.each_char.with_index do |ch, i|
    st[ch] = true
    ans += 1 if st.length == (i + 1) % 3
  end
  ans
end
