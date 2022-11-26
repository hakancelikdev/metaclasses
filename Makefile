all: amend

amend:
	git add .
	git commit --amend --no-edit
	git push origin head -f
