# LeetCode 3860 - Unique Email Groups
# https://leetcode.com/problems/unique-email-groups/

# @param {String[]} emails
# @return {Integer}
def unique_email_groups(emails)
  st = {}
  emails.each do |email|
    at = email.index("@")
    local = email[0, at]
    domain = email[(at + 1)..].downcase
    plus = local.index("+")
    local = local[0, plus] if plus
    cleaned = local.delete(".").downcase
    st[cleaned + domain] = true
  end
  st.length
end
