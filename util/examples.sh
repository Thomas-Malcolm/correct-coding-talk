#!/bin/bash

echo "Shows example input into \`pprint_eq.py\`"

OPTIONS=("Integral(x^2)"
	"Omega"
	"omega"
	"Alpha"
	"alpha"
	"phibar"
	"y==mx+c"
	"Implies(A,B)"
	"A|B"
	#"Implies(Implies(A&B,C),Implies(A,C)|Implies(B,C))"
	"~A"
	"Exists"
	"Forall"
)

for s in ${OPTIONS[@]}; do

	echo "=======";
	echo "Showing:";
	echo $s;
	echo $s | ./pprint_eq.py
done
