#! /usr/bin/env bash
set -euo pipefail

echo "expect 55"
echo "56" | sub
echo

echo "expect 57"
echo "['Five', 'Seven' ]" | add | sub
echo

echo "expect ['FIVE', 'SEVEN']"
echo "['five', 'six' ]" | add | shout
echo

echo "expect ['FIVE', 'SIX']"
echo 56 | shout
echo

echo "expect ['Five', 'Six']"
echo 56 | say

echo "expect ['five', 'six']"
echo 56 | say | whisper

echo "expect ['five', 'six']"
echo 56 | whisper
