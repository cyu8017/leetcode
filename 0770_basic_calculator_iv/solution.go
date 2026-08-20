// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

import (
	"sort"
	"strconv"
	"strings"
)

func basicCalculatorIV(expression string, evalvars []string, evalints []int) []string {
	values := map[string]int{}
	for i, v := range evalvars {
		values[v] = evalints[i]
	}
	expr := strings.ReplaceAll(expression, "(", " ( ")
	expr = strings.ReplaceAll(expr, ")", " ) ")
	tokens := strings.Fields(expr)
	pos := 0

	type key []string
	type poly map[string]int

	keyStr := func(k []string) string {
		return strings.Join(k, "\x00")
	}
	parseKey := func(s string) []string {
		if s == "" {
			return nil
		}
		return strings.Split(s, "\x00")
	}

	add := func(left, right poly) poly {
		result := poly{}
		for k, v := range left {
			result[k] += v
		}
		for k, v := range right {
			result[k] += v
		}
		out := poly{}
		for k, v := range result {
			if v != 0 {
				out[k] = v
			}
		}
		return out
	}
	negate := func(p poly) poly {
		out := poly{}
		for k, v := range p {
			out[k] = -v
		}
		return out
	}
	mul := func(left, right poly) poly {
		result := poly{}
		for lk, lv := range left {
			for rk, rv := range right {
				parts := append(append([]string{}, parseKey(lk)...), parseKey(rk)...)
				sort.Strings(parts)
				ks := keyStr(parts)
				result[ks] += lv * rv
			}
		}
		out := poly{}
		for k, v := range result {
			if v != 0 {
				out[k] = v
			}
		}
		return out
	}
	atom := func(token string) poly {
		p := poly{}
		if token[0] >= 'a' && token[0] <= 'z' {
			if v, ok := values[token]; ok {
				p[""] = v
			} else {
				p[keyStr([]string{token})] = 1
			}
		} else {
			v, _ := strconv.Atoi(token)
			p[""] = v
		}
		return p
	}

	var parseExpr func() poly
	var parseTerm func() poly
	var parseFactor func() poly

	parseFactor = func() poly {
		token := tokens[pos]
		if token == "(" {
			pos++
			p := parseExpr()
			pos++ // ')'
			return p
		}
		pos++
		return atom(token)
	}
	parseTerm = func() poly {
		p := parseFactor()
		for pos < len(tokens) && tokens[pos] == "*" {
			pos++
			p = mul(p, parseFactor())
		}
		return p
	}
	parseExpr = func() poly {
		p := parseTerm()
		for pos < len(tokens) && (tokens[pos] == "+" || tokens[pos] == "-") {
			op := tokens[pos]
			pos++
			right := parseTerm()
			if op == "+" {
				p = add(p, right)
			} else {
				p = add(p, negate(right))
			}
		}
		return p
	}

	p := parseExpr()
	keys := make([]string, 0, len(p))
	for k := range p {
		keys = append(keys, k)
	}
	sort.Slice(keys, func(i, j int) bool {
		ki, kj := parseKey(keys[i]), parseKey(keys[j])
		if len(ki) != len(kj) {
			return len(ki) > len(kj)
		}
		for t := 0; t < len(ki); t++ {
			if ki[t] != kj[t] {
				return ki[t] < kj[t]
			}
		}
		return false
	})
	answer := []string{}
	for _, k := range keys {
		coef := p[k]
		parts := parseKey(k)
		if len(parts) == 0 {
			answer = append(answer, strconv.Itoa(coef))
		} else {
			answer = append(answer, strconv.Itoa(coef)+"*"+strings.Join(parts, "*"))
		}
	}
	return answer
}
