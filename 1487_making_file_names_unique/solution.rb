# LeetCode 1487 - Making File Names Unique
# https://leetcode.com/problems/making-file-names-unique/

def get_folder_names(names)
  used = {}
  ans = []
  names.each do |name|
    if !used.key?(name)
      candidate = name
    else
      k = used[name]
      k += 1 while used.key?("#{name}(#{k})")
      candidate = "#{name}(#{k})"
      used[name] = k + 1
    end
    used[candidate] = 1
    ans << candidate
  end
  ans
end
