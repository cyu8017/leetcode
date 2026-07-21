
# @param {String} num
# @param {Integer} k
# @return {Integer}
def get_min_swaps(num, k)
  target = num.chars
  k.times { next_permutation!(target) }

  source = num.chars
  swaps = 0
  source.length.times do |i|
    next if source[i] == target[i]
    j = i
    j += 1 while source[j] != target[i]
    while j > i
      source[j], source[j - 1] = source[j - 1], source[j]
      swaps += 1
      j -= 1
    end
  end
  swaps
end

def next_permutation!(arr)
  i = arr.length - 2
  i -= 1 while i >= 0 && arr[i] >= arr[i + 1]
  if i < 0
    arr.reverse!
    return
  end
  j = arr.length - 1
  j -= 1 while arr[j] <= arr[i]
  arr[i], arr[j] = arr[j], arr[i]
  arr[(i + 1)..] = arr[(i + 1)..].reverse
end
