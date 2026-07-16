// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

import "strconv"

type Codec struct {
	urlToCode map[string]string
	codeToUrl map[string]string
	counter   int
	base      string
}

func Constructor() Codec {
	return Codec{
		urlToCode: make(map[string]string),
		codeToUrl: make(map[string]string),
		base:      "http://tinyurl.com/",
	}
}

func (this *Codec) Encode(longUrl string) string {
	if shortUrl, ok := this.urlToCode[longUrl]; ok {
		return shortUrl
	}
	code := strconv.Itoa(this.counter)
	this.counter++
	shortUrl := this.base + code
	this.urlToCode[longUrl] = shortUrl
	this.codeToUrl[shortUrl] = longUrl
	return shortUrl
}

func (this *Codec) Decode(shortUrl string) string {
	return this.codeToUrl[shortUrl]
}
