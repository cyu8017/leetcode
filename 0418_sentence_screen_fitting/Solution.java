// LeetCode 0418 - Sentence Screen Fitting

// https://leetcode.com/problems/sentence-screen-fitting/



class Solution {

    public int wordsTyping(String[] sentence, int rows, int cols) {

        int count = 0;

        int index = 0;

        int total = sentence.length;



        for (int row = 0; row < rows; row++) {

            int col = 0;



            while (true) {

                String word = sentence[index];

                int needed = word.length() + (col > 0 ? 1 : 0);



                if (col + needed > cols) {

                    break;

                }



                if (col > 0) {

                    col++;

                }



                col += word.length();

                index = (index + 1) % total;



                if (index == 0) {

                    count++;

                }

            }

        }



        return count;

    }

}
