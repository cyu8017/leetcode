// LeetCode 0483 - Smallest Good Base

// https://leetcode.com/problems/smallest-good-base/



impl Solution {

    pub fn smallest_good_base(n: String) -> String {

        let num = n.parse::<u128>().unwrap();

        for length in (2..=((num as f64).log2().floor() as i32 + 1)).rev() {

            let mut low = 2u128;

            let mut high = num - 1;

            while low <= high {

                let mid = low + (high - low) / 2;

                let mut total = 1u128;

                let mut power = 1u128;

                let mut ok = true;

                for _ in 1..length {

                    power = power.saturating_mul(mid);

                    total = total.saturating_add(power);

                    if total > num {

                        ok = false;

                        break;

                    }

                }

                if ok && total == num {

                    return mid.to_string();

                }

                if !ok || total > num {

                    high = mid - 1;

                } else {

                    low = mid + 1;

                }

            }

        }

        (num - 1).to_string()

    }

}


