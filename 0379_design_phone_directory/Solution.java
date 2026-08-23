// LeetCode 0379 - Design Phone Directory

// https://leetcode.com/problems/design-phone-directory/



import java.util.TreeSet;



class PhoneDirectory {

    private final TreeSet<Integer> available = new TreeSet<>();



    public PhoneDirectory(int maxNumbers) {

        for (int index = 0; index < maxNumbers; index++) {

            available.add(index);

        }

    }



    public int get() {

        if (available.isEmpty()) {

            return -1;

        }

        int number = available.first();

        available.remove(number);

        return number;

    }



    public boolean check(int number) {

        return available.contains(number);

    }



    public void release(int number) {

        available.add(number);

    }

}
