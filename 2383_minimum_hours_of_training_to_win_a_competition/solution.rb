# LeetCode 2383 - Minimum Hours of Training to Win a Competition
# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

# @param {Integer} initial_energy
# @param {Integer} initial_experience
# @param {Integer[]} energy
# @param {Integer[]} experience
# @return {Integer}
def min_number_of_hours(initial_energy, initial_experience, energy, experience)
  ans = 0
  en = initial_energy
  ex = initial_experience
  energy.each_index do |i|
    if en <= energy[i]
      need = energy[i] - en + 1
      ans += need
      en += need
    end
    if ex <= experience[i]
      need = experience[i] - ex + 1
      ans += need
      ex += need
    end
    en -= energy[i]
    ex += experience[i]
  end
  ans
end
