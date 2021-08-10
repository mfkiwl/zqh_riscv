# zqh_riscv整体介绍
zqh_riscv是一套开源SOC开发平台，核心部分包含处理器core、cache、片内互联总线、中断控制器、memory控制器、片内总线slave接口、片内总线master接口、片内总线device、片外总线device、时钟复位控制器、debug控制器。还包含了SOC功能验证/仿真相关的脚本程序和测试用例。除了可以运行电路仿真，平台还提供了ASIC综合脚本，可以对生成的电路做逻辑综合。支持在FPGA上的原型仿真验证。
处理器core选择开源指令集的RISC-V架构，zqh_riscv SOC的目标应用平台是各种IOT设备/嵌入式设备，处理器core不采用通用计算处理器的微架构，因此core不会集成MMU/TLB、多核cache一致性等典型AP处理器的功能。core的微架构常常选择类似于Rocket项目的结构，力求在能满足计算要求的前提下尽可能占用最低的面积与功耗。
片内互联总线选择的是tilelink总线，tilelink是开源的总线标准，它跟RISC-V指令集一样出自加州伯克利大学，跟RISC-V core的搭配最合适不过了。tilelink没有ARM的AMBA总线的名气大，但它简洁高效的结构比AXI/AHB等ARM总线更适合IOT芯片。但鉴于目前各种商业IP提供的大部分都是AMBA总线的接口，zqh_riscv也提供了tilelink接口与AMBA总线接口的转换。
作为一个集成了处理器core的SOC系统，中断控制器自必不可少，zqh_riscv平台提供了通用的本地中断控制器与平台中断控制器。本地中断控制器与特定的处理器core紧耦合。平台中断控制器是所有外设的中断控制中枢，负责把特定的外设中断请求送给特定的处理器core的外部中断引脚上。
zqh_riscv平台集成了目前各种主流的外设IP，例如UART、SPI、I2C、GPIO、PWM、JTAG、USB、Ethernet MAC、DDR、DMA引擎、时钟与复位控制器(CRG)、调试debug控制器等。除了模拟电路相关的功能，大部分数字电路相关的IP都做了整合集成，IP的接口统一为tilelink，IP既可以作为子模块集成进zqh_riscv系统，也可以单独使用并集成到任意地方。
zqh_riscv平台还提供了一套仿真脚本，可以运行仿真测试用例。综合脚本实现ASIC电路综合。可以在FPGA上跑原型仿真，zqh_riscv内会自动替换部分FPGA相关的cell。
zqh_riscv平台的实现语言以python为主，硬件描述代码使用的是PHGL，PHGL可以构建高度参数化的模块电路。
![image](doc/zqh_riscv_global_block.png)

zqh_riscv的完整硬件系统如上图所述，zqh_riscv处理器外挂tilelink master与slave接口，memory bus与IO bus分别由独立的tileink master控制。fbus slave接口用来提供外部访问的接口，例如带master接口的外设访问ITIM/DTIM memory。mem bus上挂接onchip sram、DDR3控制器、SPI XIP Flash控制器。mmio bus上挂接IO属性的配置模块与外设，支持各种主流外设: I2C、SPI、UART、PWM、USB等。目前还不支持原生ADC与DAC，模拟电路相关部分暂时无原生IP提供，但是后续规划中会随着模拟电路部分的完善而加入，print_monitor是一个仿真打印device，用来打印软件输出的debug信息。时钟产生模块由于通常有PLL等模拟电路，目前没有原生IP，但有后续规划加入。支持jtag debug接口，可以调试软件。
zqh_riscv平台提供的不仅仅是芯片硬件平台，还包含与之配套的软硬件调试脚本、测试用例、test benth、逻辑综合脚本等必不可少的部分。
全芯片的测试仿真需要test benth，test benth中提供各种标准接口的仿真模型，例如DDR、UART、I2C、SPI、eth GMII、USB host/device等。提供一整套测试用例，配合软件代码可以测试芯片系统的各个组成模块。
