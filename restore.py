import sys

with open('index.git.html', 'r', encoding='utf-16') as f:
    git_lines = f.readlines()

tien_do_start = -1
chinh_sach_start = -1

# Identify the boundaries of the tien-do section in the git history
for i, l in enumerate(git_lines):
    if '<section id="tien-do"' in l:
        tien_do_start = i
    if '<section id="chinh-sach"' in l and tien_do_start != -1:
        chinh_sach_start = i
        break

if tien_do_start == -1 or chinh_sach_start == -1:
    print('Could not find sections.')
    sys.exit(1)

# Include the wrapper lines if any (e.g., the <!-- SECTION 7 --> comments)
# Usually there are 3 lines of comments before the section tag
START_IDX = tien_do_start - 3
END_IDX = chinh_sach_start - 3

tien_do_lines = git_lines[START_IDX:END_IDX]

with open('index.html', 'r', encoding='utf-8') as f:
    current_lines = f.readlines()

faq_start = -1
for i, l in enumerate(current_lines):
    if '<section id="faq"' in l:
        faq_start = i
        break

if faq_start == -1:
    print('Could not find faq section in index.html to insert before.')
    sys.exit(1)

# Insert it before faq section (with its comments, so faq_start - 3)
INSERT_IDX = faq_start - 3

current_lines = current_lines[:INSERT_IDX] + tien_do_lines + current_lines[INSERT_IDX:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(current_lines)

print('Success')
