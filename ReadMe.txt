创建版本库
	git config --global user.name "hugh"
	git config --global user.email "hugh182@qq.com"

	git init 把这个目录变成Git可以管理的仓库
	git add "file.txt" "file1.txt" 把文件添加到仓库
	git commit -m 'you's log' 把文件提交到仓库
		初始化一个Git仓库，使用git init命令。
		添加文件到Git仓库，分两步：
		第一步，使用命令git add <file>，注意，可反复多次使用，添加多个文件；
		第二步，使用命令git commit，完成。

对比修改内容
	git status 查看仓库的当前状态
	git diff "file.txt"  对比当前文件与上一次修改后的差别
		要随时掌握工作区的状态，使用git status命令。
		如果git status告诉你有文件被修改过，用git diff可以查看修改内容。

版本回退
	git log 查看从最近到最远的提交日志
	git log --pretty=oneline 单行显示提交日志
	git log --graph [--pretty=oneline --abbrev-commit]
	git reflog 查看所有分支的所有操作记录
	git reset --hard HEAD 回退到当前版本
	git reset --hard HEAD^ 回退到上一个版本
	git reset --hard HEAD^^ 回退到上上一个版本
	git reset --hard HEAD~100 回退到上100个版本
	git reset --hard commitID 回退到指定版本号(版本号没必要写全，前几位就可以了，Git会自动去找)
		HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。
		穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。
		要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。

撤销修改
	git checkout -- "file.txt" 把file.txt文件在工作区的修改全部撤销
	git reset HEAD "file.txt"  可以把暂存区的修改撤销掉（unstage），重新放回工作区
		场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。
		场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD file，就回到了场景1，第二步按场景1操作。
		场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。
文件删除		
	git rm "file.txt" 从版本库中删除该文件
		命令git rm用于删除一个文件。如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失最近一次提交后你修改的内容。
		
创建SSH Key。
	ssh-keygen -t rsa -C "你自己的邮件地址"
		在用户主目录下，看看有没有.ssh目录，
		如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，如果已经有了，可直接跳到下一步。
		如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：ssh-keygen -t rsa -C "你自己的邮件地址"

远程仓库
	git remote add origin git@github.com:hugh125/learn_Flask.git 创建远程库
	git remote rm  origin 删除远程库
	git push -u original master 
		第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，
		还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。
	git push original master 向远程库提交，提交前在本地执行(①git add;②git commit -m 'log')
	git clone  git@github.com:hugh125/gitskills.git 克隆前，远程需要存在gitskiils库
分支管理
	git checkout -b dev ==> ①git branch dev;②git checkout dev  创建并切换到分支
	git branch 			查看当前分支，当前分支前面会标一个*号
	git branch -a		查看所有分支
	git checkout master 切换分支
	git merge dev 		合并分支，合并指定分支到当前分支
	git branch -D dev 	删除分支
	git merge --no-ff -m 'merge with no-ff' dev
		合并分支时，
		加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，
		而fast forward合并就看不出来曾经做过合并
	git stash 隐藏
	git stash pop 调出
		当手头工作没有完成时，先把工作现场git stash一下，然后去修复bug，修复后，再git stash pop，回到工作现场
	
git checkout -- file 当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时
git checkout -m

便签管理
	git tag v1.0 	创建标签
	git tag			查看所有标签
	git show v0.9	查看指定标签
	git tag -a v0.1 -m "version 0.1 released" 3628164 
		创建带有说明的标签，用-a指定标签名，-m指定说明文字
    git tag <name>用于新建一个标签，默认为HEAD，也可以指定一个commit id；
    git tag -a <tagname> -m "blablabla..."可以指定标签信息；
    git tag -s <tagname> -m "blablabla..."可以用PGP签名标签；必须首先安装gpg
    git tag	可以查看所有标签。
	
    git push origin <tagname>	可以推送一个本地标签；
    git push origin --tags		可以推送全部未推送过的本地标签；
    git tag -d <tagname>		可以删除一个本地标签；
    git push origin :refs/tags/<tagname>	可以删除一个远程标签。

自定义Git
	git config --global color.ui true	颜色显示
	.gitignore 	文本另存为.gitignore文件
		在该文件内添加Git要忽略的  文件名
	git config --global alias.st status		状态
	git config --global alias.co checkout 	切换
	git config --global alias.ci commit		提交
	git config --global alias.br branch		分支
	git config --global alias.unstage 'reset HEAD'	撤销修改
	git config --global alias.last 'log -1'	最后一次提交信息
	git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"	   日志颜色显示	
	配置Git的时候，
		加上--global是针对当前用户起作用的，
		如果不加，那只针对当前的仓库起作用。
	
配置文件：
	.git/config	每个仓库的Git配置文件
	.gitconfig	当前用户的Git配置文件	
		
		
		
		
		
		
