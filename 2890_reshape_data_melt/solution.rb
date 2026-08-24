# LeetCode 2890 - Reshape Data: Melt
# https://leetcode.com/problems/reshape-data-melt/

# @param {Object[]} report
# @return {Object[]}
def melt_table(report)
  out = []
  report.each do |r|
    if r.is_a?(Array)
      product = r[0]
      (1..4).each do |q|
        out << { "product" => product, "quarter" => "quarter_#{q}", "sales" => r[q] }
      end
    else
      %w[quarter_1 quarter_2 quarter_3 quarter_4].each do |q|
        out << { "product" => r["product"], "quarter" => q, "sales" => r[q] }
      end
    end
  end
  out
end
