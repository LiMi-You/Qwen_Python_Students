"""
学生成绩数据分析系统

本模块实现学生成绩的录入、平均分计算、等级评定及结果保存功能。
采用模块化编程思想，通过函数实现各功能，具有完善的输入合法性校验与异常处理。
"""


def input_scores(num_students: int) -> list[float]:
    """
    录入学生成绩函数
    
    根据输入的学生数量，依次录入每位学生的成绩，并校验成绩合法性。
    
    参数:
        num_students (int): 待录入的学生数量，应为正整数
    
    返回值:
        list[float]: 包含所有有效成绩的列表
    
    异常处理:
        - 若输入非数值类型，提示"输入的不是有效数值，请重新输入！"
        - 若成绩超出0-100范围，提示"成绩必须在0到100之间，请重新输入！"
        - 持续提示用户重新输入，直至录入有效成绩
    """
    scores = []
    
    for i in range(num_students):
        while True:
            try:
                user_input = input(f"请输入第 {i + 1} 位学生的成绩：")
                score = float(user_input)
                
                if score < 0 or score > 100:
                    print("成绩必须在0到100之间，请重新输入！")
                    continue
                
                scores.append(score)
                break
                
            except ValueError:
                print("输入的不是有效数值，请重新输入！")
    
    return scores


def calculate_average(scores: list[float]) -> float:
    """
    计算平均分函数
    
    计算成绩列表中所有成绩的平均分，结果保留2位小数。
    
    参数:
        scores (list[float]): 包含学生成绩的列表
    
    返回值:
        float: 平均分，保留2位小数；若列表为空则返回0.0
    """
    if len(scores) == 0:
        return 0.0
    
    average = sum(scores) / len(scores)
    return round(average, 2)


def grade_score(score: float) -> str:
    """
    成绩等级评定函数
    
    根据单个成绩数值评定对应的等级。
    
    参数:
        score (float): 待评定的成绩数值（0-100）
    
    等级划分规则:
        - 90分及以上：优秀
        - 80-89分：良好
        - 70-79分：中等
        - 60-69分：及格
        - 60分以下：不及格
    
    返回值:
        str: 对应的成绩等级字符串
    """
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 70:
        return "中等"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def save_results(scores: list[float], file_path: str = "score_result.txt") -> None:
    """
    结果保存函数
    
    将成绩列表、平均分、等级分布情况写入指定的文本文件。
    
    参数:
        scores (list[float]): 包含学生成绩的列表
        file_path (str): 文件保存路径，默认为"score_result.txt"
    
    文件内容格式:
        - 学生成绩列表：[成绩1, 成绩2, ...]
        - 全体学生的平均分：XX.XX
        - 成绩等级分布：优秀X人、良好X人、中等X人、及格X人、不及格X人
    
    异常处理:
        若保存过程中出现错误，提示"保存文件时出错：XXX"（XXX为具体错误信息）
    
    返回值:
        None
    """
    try:
        # 计算平均分
        average = calculate_average(scores)
        
        # 统计各等级人数
        grade_counts = {
            "优秀": 0,
            "良好": 0,
            "中等": 0,
            "及格": 0,
            "不及格": 0
        }
        
        for score in scores:
            grade = grade_score(score)
            grade_counts[grade] += 1
        
        # 构建文件内容
        content_lines = [
            f"学生成绩列表：{scores}",
            f"全体学生的平均分：{average:.2f}",
            f"成绩等级分布：优秀{grade_counts['优秀']}人、良好{grade_counts['良好']}人、中等{grade_counts['中等']}人、及格{grade_counts['及格']}人、不及格{grade_counts['不及格']}人"
        ]
        
        content = "\n".join(content_lines)
        
        # 写入文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
    except Exception as e:
        print(f"保存文件时出错：{e}")


def main() -> None:
    """
    主函数
    
    实现用户交互界面，展示功能菜单，接收用户输入的功能编号，
    调用对应函数完成功能，串联完整流程。
    
    菜单功能:
        1 - 录入成绩
        2 - 计算平均分
        3 - 评定单成绩等级
        4 - 保存结果
        0 - 退出程序
    
    返回值:
        None
    """
    # 存储已录入的成绩列表
    scores = []
    
    print("===== 学生成绩分析系统 =====")
    
    while True:
        print("\n功能入口：1-录入成绩 2-计算平均分 3-评定单成绩等级 4-保存结果 0-退出")
        
        choice = input("请选择功能编号：")
        
        match choice:
            case "1":
                # 录入成绩
                while True:
                    try:
                        num_input = input("请输入要录入的学生数量：")
                        num_students = int(num_input)
                        
                        if num_students <= 0:
                            print("学生数量必须是正整数，请重新输入！")
                            continue
                        
                        scores = input_scores(num_students)
                        print(f"成功录入 {len(scores)} 位学生的成绩！")
                        break
                        
                    except ValueError:
                        print("输入的不是有效数值，请重新输入！")
            
            case "2":
                # 计算平均分
                if len(scores) == 0:
                    print("请先录入成绩！")
                else:
                    average = calculate_average(scores)
                    print(f"全体学生的平均分：{average:.2f}")
            
            case "3":
                # 评定单成绩等级
                while True:
                    try:
                        user_input = input("请输入要评定的成绩：")
                        score = float(user_input)
                        
                        if score < 0 or score > 100:
                            print("成绩必须在0到100之间，请重新输入！")
                            continue
                        
                        grade = grade_score(score)
                        print(f"成绩{score:.1f}的等级：{grade}")
                        break
                        
                    except ValueError:
                        print("输入的不是有效数值，请重新输入！")
            
            case "4":
                # 保存结果
                if len(scores) == 0:
                    print("请先录入成绩！")
                else:
                    average = calculate_average(scores)
                    print(f"全体学生的平均分：{average:.2f}")
                    
                    file_path = "score_result.txt"
                    save_results(scores, file_path)
                    print(f"结果已保存至：{file_path}")
            
            case "0":
                # 退出程序
                print("程序结束！")
                break
            
            case _:
                # 无效的功能编号
                print("无效的功能编号，请输入0-4之间的数字！")


if __name__ == "__main__":
    main()
