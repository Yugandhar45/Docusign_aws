# import os.path
# from pathlib import Path
# from testData import constants
# from bs4 import BeautifulSoup
# import os
#
#
# class Test_html_to_pdf:
#
#     def test_add_logo(self):
#         root_directory = os.getcwd()
#         report_relative_path = Path(constants.htmlreport_path)
#         logo_relative_path = Path(constants.logo_path)
#         report_path = root_directory / report_relative_path
#         logo_path = root_directory / logo_relative_path
#         file_path1 = Path(report_path)
#         file_path2 = Path(logo_path)
#         html_file = str(file_path1)
#         logo_file = str(file_path2)
#         print("html_file =", html_file)
#         print("Logo_file =", logo_file)
#         with open(html_file) as file:
#             soup = BeautifulSoup(file, "html.parser")
#             h1_element = soup.find("h1")
#             image_url = os.path.abspath(logo_file)
#             image_element = soup.new_tag("img", src=image_url)
#             image_element["style"] = "width:150px;height:90px;"
#             image_element["align"] = "right"
#             text = constants.report_title
#             h1_element.clear()
#             h1_element.append(text)
#             h1_element.append(image_element)
#             updated_html_content = soup.prettify()
#             with open(html_file, "w") as file1:
#                 file1.write(updated_html_content)
#
# # import os.path
# # from testData import constants
# # from bs4 import BeautifulSoup
# # import os
# #
# #
# # class Test_html_to_pdf:
# #
# #     def test_add_logo(self):
# #         html_file = os.path.abspath(constants.htmlreport_path)
# #         with open(html_file) as file:
# #             soup = BeautifulSoup(file, "html.parser")
# #             h1_element = soup.find("h1")
# #             image_url = os.path.abspath(constants.logo_path)
# #             image_element = soup.new_tag("img", src=image_url)
# #             image_element["style"] = "width:150px;height:90px;"
# #             image_element["align"] = "right"
# #             text = constants.report_title
# #             h1_element.clear()
# #             h1_element.append(text)
# #             h1_element.append(image_element)
# #             updated_html_content = soup.prettify()
# #             with open(html_file, "w") as file1:
# #                 file1.write(updated_html_content)