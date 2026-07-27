// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

pub trait FontInfo {
    fn get_width(&self, font_size: i32, ch: char) -> i32;
    fn get_height(&self, font_size: i32) -> i32;
}

pub struct DefaultFontInfo;

impl FontInfo for DefaultFontInfo {
    fn get_width(&self, font_size: i32, _ch: char) -> i32 {
        font_size
    }
    fn get_height(&self, font_size: i32) -> i32 {
        font_size
    }
}

impl Solution {
    pub fn max_font(text: String, w: i32, h: i32, fonts: Vec<i32>, font_info: &dyn FontInfo) -> i32 {
        let (mut lo, mut hi, mut ans) = (0i32, fonts.len() as i32 - 1, -1);
        while lo <= hi {
            let mid = (lo + hi) / 2;
            let f = fonts[mid as usize];
            let mut fits = font_info.get_height(f) <= h;
            if fits {
                let width: i32 = text.chars().map(|c| font_info.get_width(f, c)).sum();
                fits = width <= w;
            }
            if fits {
                ans = f;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        ans
    }
}
