##参数定义
NAME=".cpython-37m-darwin"
a=`uname  -s`

b="Darwin"
c="centos"
d="ubuntu"
e="Linux"

if [[ $a =~ $b ]];then
    NAME=".cpython-37m-darwin"
elif [[ $a =~ $c ]];then
    NAME="centos"   #unfix
elif [[ $a =~ $d ]];then
    NAME="ubuntu"   #unfix
elif [[ $a =~ $e ]];then
    NAME=".cpython-37m-x86_64-linux-gnu"
else
    NAME="other"    #unfix
fi

##加载环境
source activate python37
mkdir lib 2>/dev/null

##编译动态链接库
python compile.py build_ext --inplace

##将so文件改名
find lib -name "*.so"|awk -F "${NAME}" '{print "mv "$0" "$1$2}'|sh

##清除不需要的文件
rm -rf build
