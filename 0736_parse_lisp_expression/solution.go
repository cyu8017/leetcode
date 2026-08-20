// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

import (
	"strconv"
	"strings"
)

func evaluate(expression string) int {
	replacer := strings.NewReplacer("(", " ( ", ")", " ) ")
	tokens := strings.Fields(replacer.Replace(expression))
	pos := 0
	isNumber := func(token string) bool {
		if token == "" {
			return false
		}
		i := 0
		if token[0] == '-' {
			i = 1
		}
		if i == len(token) {
			return false
		}
		for ; i < len(token); i++ {
			if token[i] < '0' || token[i] > '9' {
				return false
			}
		}
		return true
	}
	var parse func(env []map[string]int) int
	parse = func(env []map[string]int) int {
		token := tokens[pos]
		if token != "(" {
			pos++
			if isNumber(token) {
				v, _ := strconv.Atoi(token)
				return v
			}
			for i := len(env) - 1; i >= 0; i-- {
				if v, ok := env[i][token]; ok {
					return v
				}
			}
			panic(token)
		}
		pos++
		op := tokens[pos]
		pos++
		if op == "let" {
			env = append(env, map[string]int{})
			for tokens[pos] != ")" {
				if tokens[pos] == "(" || tokens[pos+1] == ")" {
					value := parse(env)
					pos++
					return value
				}
				variable := tokens[pos]
				pos++
				env[len(env)-1][variable] = parse(env)
			}
		}
		if op == "add" {
			left := parse(env)
			right := parse(env)
			pos++
			return left + right
		}
		if op == "mult" {
			left := parse(env)
			right := parse(env)
			pos++
			return left * right
		}
		panic(op)
	}
	return parse(nil)
}
