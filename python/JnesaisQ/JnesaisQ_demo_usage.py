# !/usr/bin/env python
# -*- coding: utf-8 -*-
from json import loads
from JnesaisQ import JnesaisQ



test_json_str =         '{"hello": "1", "zap": {"h1": "one", "h2": "two", "single": "."}}'
json_query_format_str = '{"zap": {"h1": ".*"}, "hello": ".*"}'
test_json = loads(test_json_str)
json_query_format = loads(json_query_format_str)
print("starting test_json", test_json)
print("starting json_query_format", json_query_format)

JNSQ = JnesaisQ(json_query_format)
result = JNSQ.compare(test_json,  debug_mode=0)
print("mismatches", result.json_query_mismatches)
print("matches", result.json_query_matches)
print("Overall result", JNSQ.overall_result(result))

