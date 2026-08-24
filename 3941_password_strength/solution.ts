// LeetCode 3941 - Password Strength
// https://leetcode.com/problems/password-strength/

export function passwordStrength(password: any): any {
        let st = new Set();
        for (let i = 0; i < password.length; i++) st.push(password[i]);
        let ans = 0;
        for (const ch of st) {
            if (Character.isLowerCase(ch)) ans += 1;
            else if (Character.isUpperCase(ch)) ans += 2;
            else if (((ch)=>/[0-9]/.test(ch))(ch)) ans += 3;
            else ans += 5;
        }
        return ans;
    
}
