class Images:
    """Contains the image of the game doll."""

    def __init__(self):
        """List with the doll's ascii symbols"""
        self.IMAGES = ("""\
      ╔══════════════════════════════════════╗
      ║      //                              ║
      ║     //                               ║
      ║    //                                ║
      ║   //                           
      ║  //                            
      ║ //                             
      ║//                              
      ║                                
      ║                               
      ║                               
      ║                               
      ║                               
      ║                               
      ║                               
      ║                               
      ║                                    
      ║                                
      ║                               
      ║                               
      ║                                   
      ║                             
      ║                             
      ║                             
      ║                             
      ║
      ║
      ║
      ╚════════════════════════════════════│|¤\
""", """\
      ╔══════════════════════════════════════╗
      ║      //                              ║
      ║     //                           ¤══╗║╔══¤
      ║    //                               ╚╬╝
      ║   //                             *********
      ║  //                              ░ █   █ ░
      ║ //                               ░    ┘  ░
      ║//                                ░ ~~~~~ ░
      ║                                   *******
      ║                               
      ║                               
      ║                               
      ║                               
      ║                               
      ║                               
      ║                               
      ║                                    
      ║                                
      ║                               
      ║                               
      ║                                   
      ║                             
      ║                             
      ║                             
      ║                             
      ║
      ║
      ║
      ╚════════════════════════════════════│|¤\
""", """\
      ╔══════════════════════════════════════╗
      ║      //                              ║
      ║     //                           ¤══╗║╔══¤
      ║    //                               ╚╬╝
      ║   //                             *********
      ║  //                              ░ █   █ ░
      ║ //                               ░    ┘  ░
      ║//                                ░ ~~~~~ ░
      ║                                   *******
      ║                                     ║1║
      ║                                ╔════╝0╚════╗
      ║                                ║10101101010║
      ║                                 ║001100111║ 
      ║                                  ║0100101║  
      ║                                 ║101001101║ 
      ║                                ║10110101101║
      ║                                ╚═══════════╝       
      ║                                
      ║                               
      ║                               
      ║                                   
      ║                             
      ║                             
      ║                             
      ║                             
      ║
      ║
      ║
      ╚════════════════════════════════════│|¤\
""", """\
      ╔══════════════════════════════════════╗
      ║      //                              ║
      ║     //                           ¤══╗║╔══¤
      ║    //                               ╚╬╝
      ║   //                             *********
      ║  //                              ░ █   █ ░
      ║ //                               ░    ┘  ░
      ║//                                ░ ~~~~~ ░
      ║                                   *******
      ║                                     ║1║
      ║                          ╔═════╔════╝0╚════╗
      ║                          ║1╔═══║10101101010║
      ║                         ╔╝0╚╗   ║001100111║ 
      ║                         ╚═══╝    ║0100101║  
      ║                         !!!!!   ║101001101║ 
      ║                                ║10110101101║
      ║                                ╚═══════════╝       
      ║                                
      ║                               
      ║                               
      ║                                   
      ║                             
      ║                             
      ║                             
      ║                             
      ║
      ║
      ║
      ╚════════════════════════════════════│|¤\
""", """\
      ╔══════════════════════════════════════╗
      ║      //                              ║
      ║     //                           ¤══╗║╔══¤
      ║    //                               ╚╬╝
      ║   //                             *********
      ║  //                              ░ █   █ ░
      ║ //                               ░    ┘  ░
      ║//                                ░ ~~~~~ ░
      ║                                   *******
      ║                                     ║1║
      ║                          ╔═════╔════╝0╚════╗═════╗
      ║                          ║1╔═══║10101101010║═══╗0║
      ║                         ╔╝0╚╗   ║001100111║   ╔╝1╚╗
      ║                         ╚═══╝    ║0100101║    ╚═══╝
      ║                         !!!!!   ║101001101║   !!!!!
      ║                                ║10110101101║
      ║                                ╚═══════════╝       
      ║                                
      ║                               
      ║                               
      ║                                   
      ║                             
      ║                             
      ║                             
      ║                             
      ║
      ║
      ║
      ╚════════════════════════════════════│|¤\
""", """\
      ╔══════════════════════════════════════╗
      ║      //                              ║
      ║     //                           ¤══╗║╔══¤
      ║    //                               ╚╬╝
      ║   //                             *********
      ║  //                              ░ █   █ ░
      ║ //                               ░    ┘  ░
      ║//                                ░ ~~~~~ ░
      ║                                   *******
      ║                                     ║1║
      ║                          ╔═════╔════╝0╚════╗═════╗
      ║                          ║1╔═══║10101101010║═══╗0║
      ║                         ╔╝0╚╗   ║001100111║   ╔╝1╚╗
      ║                         ╚═══╝    ║0100101║    ╚═══╝
      ║                         !!!!!   ║101001101║   !!!!!
      ║                                ║10110101101║
      ║                                ╠═══════════╝       
      ║                                ║1010║ 
      ║                                ║011║  
      ║                                ║10║   
      ║                                ╚══╝   
      ║                                ****   
      ║                               *====*  
      ║                                *¤¤*   
      ║                                 **    
      ║
      ║
      ║
      ╚════════════════════════════════════│|¤\
""", """\
      ╔══════════════════════════════════════╗
      ║      //                              ║
      ║     //                           ¤══╗║╔══¤
      ║    //                               ╚╬╝
      ║   //                             *********
      ║  //                              ░ █   █ ░
      ║ //                               ░    ┘  ░
      ║//                                ░ ~~~~~ ░
      ║                                   *******
      ║                                     ║1║
      ║                          ╔═════╔════╝0╚════╗═════╗
      ║                          ║1╔═══║10101101010║═══╗0║
      ║                         ╔╝0╚╗   ║001100111║   ╔╝1╚╗
      ║                         ╚═══╝    ║0100101║    ╚═══╝
      ║                         !!!!!   ║101001101║   !!!!!
      ║                                ║10110101101║
      ║                                ╠═══════════╣       
      ║                                ║1010║ ║0101║  
      ║                                ║011║   ║100║  
      ║                                ║10║     ║01║  
      ║                                ╚══╝     ╚══╝ 
      ║                                ****     ****
      ║                               *====*   *====*
      ║                                *¤¤*     *¤¤*
      ║                                 **       **   
      ║
      ║
      ║
      ╚════════════════════════════════════│|¤\
""")
