# LeetCode 2933 - High-Access Employees
# https://leetcode.com/problems/high-access-employees/

# @param {String[][]} access_times
# @return {String[]}
def find_high_access_employees(access_times)
  m = {}
  access_times.each do |name, t|
    hh = (t[0].ord - 48) * 10 + (t[1].ord - 48)
    mm = (t[2].ord - 48) * 10 + (t[3].ord - 48)
    m[name] ||= []
    m[name] << hh * 60 + mm
  end
  ans = []
  m.each do |name, times|
    times.sort!
    (0...times.length - 2).each do |i|
      if times[i + 2] - times[i] < 60
        ans << name
        break
      end
    end
  end
  ans.sort
end
