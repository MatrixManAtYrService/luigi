import luigi
import example

print("expect ['Five', 'Five'] (twice)")
print(luigi.call.to(example.shout, 55))
print(luigi.call.path(56, start=example.sub, end=example.shout))
print()

