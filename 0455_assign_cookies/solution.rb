# LeetCode 0455 - Assign Cookies
# https://leetcode.com/problems/assign-cookies/

class Solution
  def find_content_children(g, s)
    children = g.sort
    cookies = s.sort
    child = 0
    cookie = 0

    while child < children.length && cookie < cookies.length
      child += 1 if cookies[cookie] >= children[child]
      cookie += 1
    end

    child
  end

  alias_method :findContentChildren, :find_content_children
end
