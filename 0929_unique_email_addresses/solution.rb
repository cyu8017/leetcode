# LeetCode 0929 - Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses/

# @param {String[]} emails
# @return {Integer}
def num_unique_emails(emails)
  normalized = {}
  emails.each do |email|
    local, domain = email.split("@", 2)
    local = local.split("+", 2)[0].delete(".")
    normalized["#{local}@#{domain}"] = true
  end
  normalized.length
end
