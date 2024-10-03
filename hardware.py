import wmi # pip install wmi
c = wmi.WMI()

def show(element):
    for item in element:
        print(item)

# A classe WMI Win32_1394Controller representa os recursos e o gerenciamento de um controlador 1394. O IEEE 1394 é uma especificação para um barramento serial de alta velocidade.
show(c.Win32_1394Controller())

# A classe WMI de associação Win32_1394ControllerDevice relaciona o controlador de barramento serial de alta velocidade (IEEE 1394 Firewire) e a instância CIM_LogicalDevice conectada a ele. Esse barramento serial fornece conectividade aprimorada para uma ampla variedade de dispositivos, incluindo componentes de áudio ou vídeo do consumidor, periféricos de armazenamento, outros computadores e dispositivos portáteis. O IEEE 1394 foi adotado pelo setor de eletrônicos de consumo e fornece uma interface de expansão compatível com Plug and Play.
show(c.Win32_1394ControllerDevice())

# A classe WMI Win32_Fan representa as propriedades de um dispositivo ventilador no sistema do computador. Por exemplo, o ventilador de resfriamento da CPU.
show(c.Win32_Fan())

# A classe WMIWin32_HeatPipe representa as propriedades de um dispositivo de resfriamento de pipe de calor.
show(c.Win32_HeatPipe())

# A classe WMI Win32_Refrigeration representa as propriedades de um dispositivo de refrigeração.
show(c.Win32_Refrigeration())

# A classe WMI Win32_TemperatureProbe representa as propriedades de um sensor de temperatura (termômetro eletrônico).
show(c.Win32_TemperatureProbe())
## OBS.: A maioria das informações fornecidas pela classe WMI Win32_TemperatureProbe vem do SMBIOS. Leituras em tempo real para a propriedade CurrentReading não podem ser extraídas de tabelas SMBIOS. Por esse motivo, as implementações atuais do WMI não preenchem a propriedade CurrentReading . A presença da propriedade CurrentReading é reservada para uso futuro.

# A classe WMI de associação Win32_AssociatedProcessorMemory relaciona um processador e sua memória de cache.
show(c.Win32_AssociatedProcessorMemory())

# A classe WMI Win32_AutochkSetting representa as configurações para a operação de verificação automática de um disco.
show(c.Win32_AutochkSetting())

# A classe WMI Win32_BaseBoard representa um quadro base, que também é conhecido como placa-mãe ou placa-mãe do sistema.
show(c.Win32_BaseBoard())

# A classe WMI Win32_Battery representa uma bateria conectada ao sistema do computador.
show(c.Win32_Battery())

# A classe WMI Win32_BIOS representa os atributos dos BIOS (serviços básicos de entrada/saída) do sistema de computador instalados em um computador.
show(c.Win32_BIOS())

# A classe WMI Win32_Bus representa um barramento físico, conforme visto por um computador que executa um sistema operacional Windows. Qualquer instância de um barramento do Windows é um descendente (ou membro) dessa classe.
show(c.Win32_Bus())

# A classe WMI Win32_CacheMemory representa memória de cache interna e externa em um sistema de computador.
show(c.Win32_CacheMemory())

# A classe WMI Win32_CDROMDrive representa uma unidade CD-ROM em um sistema de computador que executa o Windows.
show(c.Win32_CDROMDrive())
## OBS.: Lembre-se de que o nome da unidade não corresponde à letra da unidade lógica atribuída ao dispositivo.

# A classe WMI de associação Win32_CIMLogicalDeviceCIMDataFile relaciona dispositivos lógicos e arquivos de dados, indicando os arquivos de driver usados pelo dispositivo. Essa classe é usada para descobrir quais drivers de dispositivo um dispositivo usa.
show(c.Win32_CIMLogicalDeviceCIMDataFile())

# A classe WMI de associação Win32_ComputerSystemProcessor relaciona um sistema de computador e um processador em execução nesse sistema.
show(c.Win32_ComputerSystemProcessor())

# A classe WMI Win32_CurrentProbe representa as propriedades de um sensor de monitoramento atual (ammeter).
show(c.Win32_CurrentProbe())

# A classe WMI Win32_DesktopMonitor representa o tipo de monitor ou dispositivo de exibição anexado ao sistema do computador.
show(c.Win32_DesktopMonitor())
## OBS.: O hardware que não é compatível com o WDDM (Modelo de Driver de Exibição do Windows) retorna valores de propriedade imprecisos para instâncias dessa classe.

