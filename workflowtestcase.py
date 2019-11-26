#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
根据业务流程图，自动化快速生成全路径覆盖测试用例
'''
def search_graph(graph: dict, start, end):
    _ret = []
    generate_path(graph, [start], end, _ret)
    # 这一步的排序可有可无，只不过为了显示好看
    _ret.sort(key=lambda x: len(x))
    return _ret

def generate_path(graph: dict, path, end, ret: list):
    _state = path[-1]
    # 如果起始点和终点是同一个位置，则结束
    if _state == end:
        ret.append(path)
    else:
        for _item in graph[_state]:
            if _item not in path:
                # path + [_item] 就是递归调用的关键参数，path的组成
                generate_path(graph, path + [_item], end, ret)


if __name__ == '__main__':
    # 根据业务流程图，画出节点与路径图，然后拆解成字典
    _GRAPH = {'1.拟稿': ['2.部门主任核稿', '2.1.部室核稿'],
              '2.1.部室核稿': ['2.部门主任核稿'],
             '2.部门主任核稿': ['3.相关部门会签','4.办公室核稿'],
             '3.相关部门会签': ['2.部门主任核稿'],
             '4.办公室核稿': ['5.办公室主任核签'],
             '5.办公室主任核签': ['5.1.协管领导核签', '6.分管领导核签', '7.分管领导签发'],
             '5.1.协管领导核签': ['10.办公室排版套红'],
             '6.分管领导核签': ['9.党委书记签发','12.归档'],
             '7.分管领导签发': ['10.办公室排版套红', '12.归档'],
             '9.党委书记签发': ['10.办公室排版套红','12.归档'],
             '10.办公室排版套红': ['11.分发'],
             '11.分发': ['11.1.补签','12.归档'],
             '11.1.补签': ['7.分管领导签发','9.党委书记签发']}

    _ret = search_graph(_GRAPH, '1.拟稿', '12.归档')
    print("******************")
    print(' 总局行政发文流程覆盖测试用例：')
    print("******************")
    sum = 0
    for i in _ret:
        case = '->'.join(i)
        print(case)
        sum += 1
    print('总共设计出%s条测试用例！' % sum)