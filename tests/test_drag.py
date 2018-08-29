# def drag_obj(self,item, target):
#     with open("C:\\Users\\ssoloshchenko\\job_control\\tests\\jquery_load_helper.js") as f:
#         load_jquery_js = f.read()
#     with open("C:\\Users\\ssoloshchenko\\job_control\\tests\\drag_and_drop_helper.js") as f:
#         drag_and_drop_js = f.read()
#     driver.execute_async_script(load_jquery_js)
#     driver.execute_script(drag_and_drop_js + "$('%s').simulateDragDrop({ dropTarget: '%s'});" % (item, target))

# def drag_obj(self):
#     s('a.mat-tab-link:nth-child(3)').click()
#     # time.sleep(2)
#     # # s('#jobsListJobSendButton1').click()
#     # with open("C:\\Users\\ssoloshchenko\\job_control\\tests\\jquery_load_helper.js") as f:
#     #     load_jquery_js = f.read()
#     # with open("C:\\Users\\ssoloshchenko\\job_control\\tests\\drag_and_drop_helper.js") as f:
#     #     drag_and_drop_js = f.read()
#     # driver.execute_async_script(load_jquery_js)
#     #
#     # driver.execute_script(drag_and_drop_js + "$('#jobsListJob1').simulateDragDrop({ dropTarget: '#laserWorktopCanvas'});")
#     driver.find_element_by_css_selector('a.mat-tab-link:nth-child(3)').click()
#     time.sleep(2)
#     job = driver.find_element_by_css_selector('#jobsListJob1')
#
#     canvas = driver.find_element_by_css_selector('#laserWorktopCanvas')
#     print(canvas.location)
#     # action.move_by_offset(450, 200).perform()
#
#     action = ActionChains(driver)
#
#     # action = ActionChains(driver).click_and_hold(job).move_to_element_with_offset(canvas, 300, 200).release(job)
#     action.drag_and_drop_by_offset(job, 300, 300)
#     # action.move_by_offset(200, 200)
#     # action.release(job).perform()
#     action.perform()
