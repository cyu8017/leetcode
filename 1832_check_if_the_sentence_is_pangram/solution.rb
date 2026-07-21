
# @param {String} sentence
# @return {Boolean}
def check_if_pangram(sentence)
  sentence.chars.uniq.length == 26
end
