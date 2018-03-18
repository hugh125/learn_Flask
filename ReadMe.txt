# bash git_push.sh
# git remote add origin git@github.com:hugh125/learn_Flask.git

# 1、克隆远程仓库，修改为自己的工作路径名
# 2、删除不需要的文件
# 3、提交修改后的文件
# git clone  git@github.com:hugh125/learn_Flask.git
# git rm -r --cached *
# git commit -m 'del_all_file'
# git push origin master

git add *
git commit -m 'push_log'
git push origin master
git status