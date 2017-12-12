#coding:utf-8
js="""
function makeKey_9(str){var str=str.substr(5,5*5)+"5"+str.substr(1,2)+"1"+str.substr((5+1)*(5+1),3);var a=str.substr(5)+str.substr(4);var b=str.substr(12)+a.substr(-6);var c=hex_sha1(str.substr(4))+a.substr(6);return hex_md5(c).substr(4,24)}

function makeKey_10(str){var str=encode(str.substr(5,5*5-1)+"5")+str.substr(1,2)+str.substr((5+1)*(5+1),3);var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%16))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))}a=long+""+str.substr(4);var b=hex_md5(str.substr(1))+hex_sha1(a.substr(5));return hex_md5(b).substr(4,24)}function makeKey_11(str){var str=str.substr(5,5*5-1)+"2"+str.substr(1,2)+str.substr((5+1)*(5+1),3);var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%16))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))}a=long+""+str.substr(2);var b=str.substr(1)+hex_sha1(a.substr(5));return hex_md5(b).substr(2,24)}function makeKey_136(str){return hex_md5(makeKey_18(str)+makeKey_1(str)).substr(1,24)}function makeKey_137(str){return hex_md5(makeKey_19(str)+makeKey_14(str)).substr(2,24)}function makeKey_138(str){return hex_md5(makeKey_0(str)+makeKey_15(str)).substr(3,24)}function makeKey_139(str){return hex_md5(makeKey_1(str)+makeKey_16(str)).substr(4,24)}function makeKey_140(str){return hex_md5(makeKey_4(str)+makeKey_9(str)).substr(1,24)}function makeKey_141(str){return hex_md5(makeKey_5(str)+makeKey_10(str)).substr(2,24)}function makeKey_142(str){return hex_md5(makeKey_3(str)+makeKey_17(str)).substr(3,24)}function makeKey_0(str){var str=str.substr(5,5*5)+str.substr((5+1)*(5+1),3);var a=str.substr(5)+str.substr(-4);var b=str.substr(4)+a.substr(-6);return hex_md5(str).substr(4,24)}function makeKey_1(str){var str=str.substr(5,5*5)+"5"+str.substr(1,2)+"1"+str.substr((5+1)*(5+1),3);var a=str.substr(5)+str.substr(4);var b=str.substr(12)+a.substr(-6);var c=str.substr(4)+a.substr(6);return hex_md5(c).substr(4,24)}function makeKey_2(str){var str=str.substr(5,5*5)+"15"+str.substr(1,2)+str.substr((5+1)*(5+1),3);var a=strToLong(str.substr(5))+str.substr(4);var b=strToLong(str.substr(5))+str.substr(4);var c=str.substr(4)+b.substr(5);return hex_md5(c).substr(1,24)}function makeKey_16(str){var str=str.substr(5,5*5-1)+"2"+str.substr(1,2)+"-"+"5";var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%11))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))+i}a=long+""+str.substr(2);var b=encode(a.substr(1))+strToLongEn2(str.substr(5),5)+str.substr(2,3);return hex_md5(b).substr(2,24)}function makeKey_17(str){var str=str.substr(5,5*5-1)+"7"+str.substr(1,2)+"-"+"5";var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%11))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))+i}a=long+""+str.substr(2);var b=encode(a.substr(1))+strToLongEn2(str.substr(5),5+1)+str.substr(2+5,3);return hex_md5(b).substr(0,24)}function makeKey_18(str){var str=str.substr(5,5*5-1)+"7"+str.substr(1,2)+"5"+str.substr(2+5,3);var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%11))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))+i}a=long+""+str.substr(2);var b=a.substr(1)+strToLongEn2(str.substr(5),5+1)+str.substr(2+5,3);return hex_md5(b).substr(0,24)}function makeKey_19(str){var str=str.substr(5,5*5-1)+"7"+str.substr(5,2)+"5"+str.substr(2+5,3);var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%11))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))+i}a=long+""+str.substr(2);var b=a.substr(1)+strToLongEn3(str.substr(5),5-1)+str.substr(2+5,3);return hex_md5(b).substr(0,24)}function makeKey_20(str){return hex_md5(makeKey_10(str)+makeKey_5(str)).substr(1,24)}function makeKey_21(str){return hex_md5(makeKey_11(str)+makeKey_3(str)).substr(2,24)}function makeKey_22(str){return hex_md5(makeKey_14(str)+makeKey_19(str)).substr(3,24)}function makeKey_23(str){return hex_md5(makeKey_15(str)+makeKey_0(str)).substr(4,24)}function makeKey_24(str){return hex_md5(makeKey_16(str)+makeKey_1(str)).substr(1,24)}function makeKey_25(str){return hex_md5(makeKey_9(str)+makeKey_4(str)).substr(2,24)}function makeKey_26(str){return hex_md5(makeKey_10(str)+makeKey_5(str)).substr(3,24)}function makeKey_27(str){return hex_md5(makeKey_17(str)+makeKey_3(str)).substr(4,24)}function makeKey_28(str){return hex_md5(makeKey_18(str)+makeKey_7(str)).substr(1,24)}function makeKey_29(str){return hex_md5(makeKey_19(str)+makeKey_3(str)).substr(2,24)}function makeKey_30(str){return hex_md5(makeKey_0(str)+makeKey_7(str)).substr(3,24)}function makeKey_31(str){return hex_md5(makeKey_1(str)+makeKey_8(str)).substr(4,24)}function makeKey_32(str){return hex_md5(makeKey_4(str)+makeKey_14(str)).substr(3,24)}function makeKey_33(str){return hex_md5(makeKey_5(str)+makeKey_15(str)).substr(4,24)}function makeKey_34(str){return hex_md5(makeKey_3(str)+makeKey_16(str)).substr(1,24)}function makeKey_7(str){var str=encode(str.substr(5,5*4)+"55"+str.substr(1,2))+str.substr((5+1)*(5+1),3);var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%16+5))+3+5}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))}a=long+""+str.substr(4);var b=hex_md5(str.substr(1))+strToLong(a.substr(5));return hex_md5(b).substr(3,24)}function makeKey_8(str){var str=encode(str.substr(5,5*5-1)+"5"+"-"+"5")+str.substr(1,2)+str.substr((5+1)*(5+1),3);var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%16))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))}a=long+""+str.substr(4);var b=hex_md5(str.substr(1))+strToLongEn(a.substr(5));return hex_md5(b).substr(4,24)}function makeKey_143(str){return hex_md5(makeKey_7(str)+makeKey_18(str)).substr(4,24)}function makeKey_144(str){return hex_md5(makeKey_17(str)+makeKey_19(str)).substr(1,24)}function makeKey_145(str){return hex_md5(makeKey_18(str)+makeKey_0(str)).substr(2,24)}function makeKey_146(str){return hex_md5(makeKey_19(str)+makeKey_1(str)).substr(3,24)}function makeKey_147(str){return hex_md5(makeKey_0(str)+makeKey_4(str)).substr(4,24)}function makeKey_148(str){return hex_md5(makeKey_1(str)+makeKey_5(str)).substr(3,24)}function makeKey_149(str){return hex_md5(makeKey_4(str)+makeKey_3(str)).substr(4,24)}function makeKey_150(str){return hex_md5(makeKey_14(str)+makeKey_19(str)).substr(1,24)}function makeKey_151(str){return hex_md5(makeKey_15(str)+makeKey_0(str)).substr(2,24)}function makeKey_152(str){return hex_md5(makeKey_16(str)+makeKey_1(str)).substr(3,24)}function makeKey_12(str){var str=str.substr(5,5*5-1)+str.substr((5+1)*(5+1),3)+"2"+str.substr(1,2);var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%16))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))}a=long+""+str.substr(2);var b=str.substr(1)+hex_sha1(str.substr(5));return hex_md5(b).substr(1,24)}function makeKey_13(str){var str=str.substr(5,5*5-1)+"2"+str.substr(1,2);var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%16))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))}a=long+""+str.substr(2);var b=encode(str.substr(1)+hex_sha1(str.substr(5)));return hex_md5(b).substr(1,24)}function makeKey_14(str){var str=str.substr(5,5*5-1)+"2"+str.substr(1,2);var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%16))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))}a=long+""+str.substr(2);var b=encode(str.substr(1)+str.substr(5)+str.substr(1,3));return hex_sha1(b).substr(1,24)}function makeKey_181(str){return hex_md5(makeKey_19(str)+makeKey_15(str)).substr(1,24)}function makeKey_182(str){return hex_md5(makeKey_0(str)+makeKey_16(str)).substr(2,24)}function makeKey_183(str){return hex_md5(makeKey_1(str)+makeKey_9(str)).substr(3,24)}function makeKey_184(str){return hex_md5(makeKey_4(str)+makeKey_10(str)).substr(4,24)}function makeKey_185(str){return hex_md5(makeKey_14(str)+makeKey_17(str)).substr(3,24)}function makeKey_186(str){return hex_md5(makeKey_15(str)+makeKey_18(str)).substr(4,24)}function makeKey_187(str){return hex_md5(makeKey_16(str)+makeKey_19(str)).substr(4,24)}function makeKey_188(str){return hex_md5(makeKey_9(str)+makeKey_0(str)).substr(1,24)}function makeKey_189(str){return hex_md5(makeKey_10(str)+makeKey_1(str)).substr(2,24)}function makeKey_190(str){return hex_md5(makeKey_17(str)+makeKey_4(str)).substr(3,24)}function makeKey_191(str){return hex_md5(makeKey_18(str)+makeKey_19(str)).substr(4,24)}function makeKey_192(str){return hex_md5(makeKey_19(str)+makeKey_0(str)).substr(1,24)}function makeKey_193(str){return hex_md5(makeKey_0(str)+makeKey_1(str)).substr(2,24)}function makeKey_194(str){return hex_md5(makeKey_1(str)+makeKey_4(str)).substr(3,24)}function makeKey_195(str){return hex_md5(makeKey_4(str)+makeKey_14(str)).substr(4,24)}function makeKey_196(str){return hex_md5(makeKey_5(str)+makeKey_15(str)).substr(3,24)}function makeKey_197(str){return hex_md5(makeKey_3(str)+makeKey_16(str)).substr(4,24)}function makeKey_198(str){return hex_md5(makeKey_3(str)+makeKey_9(str)).substr(1,24)}function makeKey_199(str){return hex_md5(makeKey_7(str)+makeKey_1(str)).substr(2,24)}function makeKey_15(str){var str=str.substr(5,5*5-1)+"2"+str.substr(1,2);var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%16))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))}a=long+""+str.substr(2);var b=encode(a.substr(1)+str.substr(5)+str.substr(2,3));return hex_sha1(b).substr(1,24)}function makeKey_130(str){return hex_md5(makeKey_14(str)+makeKey_7(str)).substr(3,24)}function makeKey_131(str){return hex_md5(makeKey_15(str)+makeKey_10(str)).substr(4,24)}function makeKey_132(str){return hex_md5(makeKey_16(str)+makeKey_17(str)).substr(3,24)}function makeKey_133(str){return hex_md5(makeKey_9(str)+makeKey_18(str)).substr(4,24)}function makeKey_134(str){return hex_md5(makeKey_10(str)+makeKey_19(str)).substr(1,24)}function makeKey_135(str){return hex_md5(makeKey_17(str)+makeKey_0(str)).substr(2,24)}function makeKey_153(str){return hex_md5(makeKey_9(str)+makeKey_4(str)).substr(1,24)}function makeKey_154(str){return hex_md5(makeKey_10(str)+makeKey_5(str)).substr(1,24)}function makeKey_155(str){return hex_md5(makeKey_17(str)+makeKey_3(str)).substr(2,24)}function makeKey_156(str){return hex_md5(makeKey_18(str)+makeKey_7(str)).substr(3,24)}function makeKey_157(str){return hex_md5(makeKey_19(str)+makeKey_3(str)).substr(4,24)}function makeKey_158(str){return hex_md5(makeKey_0(str)+makeKey_7(str)).substr(1,24)}function makeKey_159(str){return hex_md5(makeKey_1(str)+makeKey_8(str)).substr(2,24)}function makeKey_160(str){return hex_md5(makeKey_4(str)+makeKey_14(str)).substr(3,24)}function makeKey_161(str){return hex_md5(makeKey_19(str)+makeKey_15(str)).substr(4,24)}function makeKey_162(str){return hex_md5(makeKey_0(str)+makeKey_16(str)).substr(1,24)}function makeKey_163(str){return hex_md5(makeKey_1(str)+makeKey_9(str)).substr(2,24)}function makeKey_164(str){return hex_md5(makeKey_4(str)+makeKey_10(str)).substr(3,24)}function makeKey_165(str){return hex_md5(makeKey_5(str)+makeKey_17(str)).substr(4,24)}function makeKey_166(str){return hex_md5(makeKey_3(str)+makeKey_18(str)).substr(3,24)}function makeKey_167(str){return hex_md5(makeKey_7(str)+makeKey_19(str)).substr(4,24)}function makeKey_168(str){return hex_md5(makeKey_0(str)+makeKey_0(str)).substr(1,24)}function makeKey_169(str){return hex_md5(makeKey_1(str)+makeKey_1(str)).substr(2,24)}function makeKey_170(str){return hex_md5(makeKey_4(str)+makeKey_4(str)).substr(3,24)}function makeKey_171(str){return hex_md5(makeKey_17(str)+makeKey_5(str)).substr(1,24)}function makeKey_172(str){return hex_md5(makeKey_18(str)+makeKey_3(str)).substr(2,24)}function makeKey_173(str){return hex_md5(makeKey_19(str)+makeKey_7(str)).substr(3,24)}function makeKey_174(str){return hex_md5(makeKey_0(str)+makeKey_17(str)).substr(4,24)}function makeKey_175(str){return hex_md5(makeKey_1(str)+makeKey_18(str)).substr(1,24)}function makeKey_176(str){return hex_md5(makeKey_4(str)+makeKey_19(str)).substr(2,24)}function makeKey_35(str){return hex_md5(makeKey_7(str)+makeKey_9(str)).substr(2,24)}function makeKey_36(str){return hex_md5(makeKey_8(str)+makeKey_10(str)).substr(3,24)}function makeKey_37(str){return hex_md5(makeKey_6(str)+makeKey_17(str)).substr(1,24)}function makeKey_38(str){return hex_md5(makeKey_12(str)+makeKey_18(str)).substr(2,24)}function makeKey_39(str){return hex_md5(makeKey_14(str)+makeKey_19(str)).substr(3,24)}function makeKey_40(str){return hex_md5(makeKey_15(str)+makeKey_0(str)).substr(4,24)}function makeKey_41(str){return hex_md5(makeKey_16(str)+makeKey_1(str)).substr(3,24)}function makeKey_42(str){return hex_md5(makeKey_9(str)+makeKey_4(str)).substr(4,24)}function makeKey_43(str){return hex_md5(makeKey_10(str)+makeKey_5(str)).substr(1,24)}function makeKey_44(str){return hex_md5(makeKey_17(str)+makeKey_3(str)).substr(2,24)}function makeKey_45(str){return hex_md5(makeKey_18(str)+makeKey_7(str)).substr(3,24)}function makeKey_46(str){return hex_md5(makeKey_19(str)+makeKey_17(str)).substr(4,24)}function makeKey_47(str){return hex_md5(makeKey_0(str)+makeKey_18(str)).substr(1,24)}function makeKey_48(str){return hex_md5(makeKey_1(str)+makeKey_19(str)).substr(2,24)}function makeKey_49(str){return hex_md5(makeKey_4(str)+makeKey_0(str)).substr(3,24)}function makeKey_50(str){return hex_md5(makeKey_5(str)+makeKey_1(str)).substr(4,24)}function makeKey_51(str){return hex_md5(makeKey_3(str)+makeKey_4(str)).substr(1,24)}function makeKey_52(str){return hex_md5(makeKey_7(str)+makeKey_14(str)).substr(2,24)}function makeKey_53(str){return hex_md5(makeKey_12(str)+makeKey_15(str)).substr(3,24)}function makeKey_54(str){return hex_md5(makeKey_14(str)+makeKey_16(str)).substr(4,24)}function makeKey_55(str){return hex_md5(makeKey_15(str)+makeKey_9(str)).substr(3,24)}function makeKey_56(str){return hex_md5(makeKey_16(str)+makeKey_10(str)).substr(4,24)}function makeKey_57(str){return hex_md5(makeKey_9(str)+makeKey_17(str)).substr(1,24)}function makeKey_58(str){return hex_md5(makeKey_10(str)+makeKey_18(str)).substr(2,24)}function makeKey_59(str){return hex_md5(makeKey_17(str)+makeKey_19(str)).substr(3,24)}function makeKey_60(str){return hex_md5(makeKey_18(str)+makeKey_0(str)).substr(1,24)}function makeKey_61(str){return hex_md5(makeKey_19(str)+makeKey_1(str)).substr(2,24)}function makeKey_62(str){return hex_md5(makeKey_0(str)+makeKey_4(str)).substr(3,24)}function makeKey_63(str){return hex_md5(makeKey_1(str)+makeKey_19(str)).substr(4,24)}function makeKey_64(str){return hex_md5(makeKey_4(str)+makeKey_0(str)).substr(3,24)}function makeKey_65(str){return hex_md5(makeKey_14(str)+makeKey_1(str)).substr(1,24)}function makeKey_66(str){return hex_md5(makeKey_15(str)+makeKey_4(str)).substr(2,24)}function makeKey_67(str){return hex_md5(makeKey_16(str)+makeKey_5(str)).substr(3,24)}function makeKey_68(str){return hex_md5(makeKey_9(str)+makeKey_3(str)).substr(4,24)}function makeKey_69(str){return hex_md5(makeKey_10(str)+makeKey_7(str)).substr(1,24)}function makeKey_70(str){return hex_md5(makeKey_17(str)+makeKey_0(str)).substr(2,24)}function makeKey_71(str){return hex_md5(makeKey_18(str)+makeKey_1(str)).substr(3,24)}function makeKey_72(str){return hex_md5(makeKey_19(str)+makeKey_4(str)).substr(4,24)}function makeKey_73(str){return hex_md5(makeKey_0(str)+makeKey_17(str)).substr(1,24)}function makeKey_74(str){return hex_md5(makeKey_1(str)+makeKey_18(str)).substr(2,24)}function makeKey_75(str){return hex_md5(makeKey_14(str)+makeKey_19(str)).substr(3,24)}function makeKey_76(str){return hex_md5(makeKey_15(str)+makeKey_0(str)).substr(4,24)}function makeKey_77(str){return hex_md5(makeKey_16(str)+makeKey_1(str)).substr(3,24)}function makeKey_78(str){return hex_md5(makeKey_9(str)+makeKey_4(str)).substr(4,24)}function makeKey_79(str){return hex_md5(makeKey_10(str)+makeKey_9(str)).substr(1,24)}function makeKey_80(str){return hex_md5(makeKey_17(str)+makeKey_10(str)).substr(2,24)}function makeKey_81(str){return hex_md5(makeKey_18(str)+makeKey_17(str)).substr(3,24)}function makeKey_82(str){return hex_md5(makeKey_14(str)+makeKey_18(str)).substr(1,24)}function makeKey_83(str){return hex_md5(makeKey_15(str)+makeKey_19(str)).substr(4,24)}function makeKey_84(str){return hex_md5(makeKey_16(str)+makeKey_0(str)).substr(1,24)}function makeKey_85(str){return hex_md5(makeKey_9(str)+makeKey_1(str)).substr(2,24)}function makeKey_86(str){return hex_md5(makeKey_10(str)+makeKey_4(str)).substr(3,24)}function makeKey_87(str){return hex_md5(makeKey_14(str)+makeKey_14(str)).substr(4,24)}function makeKey_88(str){return hex_md5(makeKey_15(str)+makeKey_15(str)).substr(1,24)}function makeKey_89(str){return hex_md5(makeKey_16(str)+makeKey_16(str)).substr(2,24)}function makeKey_90(str){return hex_md5(makeKey_9(str)+makeKey_9(str)).substr(3,24)}function makeKey_91(str){return hex_md5(makeKey_10(str)+makeKey_10(str)).substr(4,24)}function makeKey_92(str){return hex_md5(makeKey_17(str)+makeKey_17(str)).substr(3,24)}function makeKey_93(str){return hex_md5(makeKey_18(str)+makeKey_18(str)).substr(4,24)}function makeKey_94(str){return hex_md5(makeKey_19(str)+makeKey_19(str)).substr(1,24)}function makeKey_95(str){return hex_md5(makeKey_0(str)+makeKey_0(str)).substr(2,24)}function makeKey_96(str){return hex_md5(makeKey_1(str)+makeKey_1(str)).substr(3,24)}function makeKey_97(str){return hex_md5(makeKey_4(str)+makeKey_4(str)).substr(4,24)}function makeKey_98(str){return hex_md5(makeKey_5(str)+makeKey_5(str)).substr(3,24)}function makeKey_99(str){return hex_md5(makeKey_3(str)+makeKey_3(str)).substr(4,24)}function makeKey_100(str){return hex_md5(makeKey_7(str)+makeKey_3(str)).substr(1,24)}function makeKey_101(str){return hex_md5(makeKey_10(str)+makeKey_7(str)).substr(2,24)}function makeKey_102(str){return hex_md5(makeKey_17(str)+makeKey_18(str)).substr(1,24)}function makeKey_103(str){return hex_md5(makeKey_18(str)+makeKey_19(str)).substr(2,24)}function makeKey_104(str){return hex_md5(makeKey_19(str)+makeKey_0(str)).substr(3,24)}function makeKey_105(str){return hex_md5(makeKey_0(str)+makeKey_0(str)).substr(4,24)}function makeKey_106(str){return hex_md5(makeKey_1(str)+makeKey_1(str)).substr(1,24)}function makeKey_107(str){return hex_md5(makeKey_14(str)+makeKey_14(str)).substr(2,24)}function makeKey_108(str){return hex_md5(makeKey_15(str)+makeKey_15(str)).substr(3,24)}function makeKey_109(str){return hex_md5(makeKey_16(str)+makeKey_16(str)).substr(4,24)}function makeKey_110(str){return hex_md5(makeKey_9(str)+makeKey_9(str)).substr(1,24)}function makeKey_111(str){return hex_md5(makeKey_10(str)+makeKey_10(str)).substr(2,24)}function makeKey_112(str){return hex_md5(makeKey_17(str)+makeKey_17(str)).substr(3,24)}function makeKey_113(str){return hex_md5(makeKey_18(str)+makeKey_18(str)).substr(4,24)}function makeKey_114(str){return hex_md5(makeKey_19(str)+makeKey_19(str)).substr(3,24)}function makeKey_115(str){return hex_md5(makeKey_0(str)+makeKey_0(str)).substr(4,24)}function makeKey_116(str){return hex_md5(makeKey_1(str)+makeKey_1(str)).substr(1,24)}function makeKey_117(str){return hex_md5(makeKey_4(str)+makeKey_4(str)).substr(2,24)}function makeKey_118(str){return hex_md5(makeKey_5(str)+makeKey_15(str)).substr(3,24)}function makeKey_119(str){return hex_md5(makeKey_3(str)+makeKey_16(str)).substr(1,24)}function makeKey_120(str){return hex_md5(makeKey_19(str)+makeKey_9(str)).substr(1,24)}function makeKey_121(str){return hex_md5(makeKey_0(str)+makeKey_10(str)).substr(2,24)}function makeKey_122(str){return hex_md5(makeKey_1(str)+makeKey_17(str)).substr(3,24)}function makeKey_123(str){return hex_md5(makeKey_4(str)+makeKey_18(str)).substr(4,24)}function makeKey_124(str){return hex_md5(makeKey_5(str)+makeKey_19(str)).substr(1,24)}function makeKey_125(str){return hex_md5(makeKey_3(str)+makeKey_0(str)).substr(2,24)}function makeKey_3(str){var str=str.substr(5,5*5)+"15"+str.substr(1,2)+str.substr((5+1)*(5+1),3);var a=strToLongEn(str.substr(5))+str.substr(4);var b=str.substr(4)+a.substr(5);var c=strToLong(str.substr(5))+str.substr(4);return hex_md5(b).substr(3,24)}function makeKey_4(str){var str=str.substr(5,5*5)+"2"+str.substr(1,2)+str.substr((5+1)*(5+1),3);var long=0;for(var i=0;i<str.substr(1).length;i++){long+=(str.charCodeAt(i)<<(i%16))}var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))+i}a=long+""+str.substr(4);var b=hex_md5(str.substr(1))+strToLong(a.substr(5));return hex_md5(b).substr(3,24)}function makeKey_5(str){var str=encode(str.substr(5,5*5)+str.substr(1,2)+"1")+str.substr((5+1)*(5+1),3);var a=strToLongEn(str.substr(4,10))+str.substr(-4);var b=hex_md5(str.substr(4))+a.substr(2);var a=str.substr(3);var c=strToLong(str.substr(5))+str.substr(4);var aa=long+str.substr(4);var long=0;for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%12))+i}a=long+""+str.substr(4);return hex_md5(str).substr(4,24)}function makeKey_6(str){var str=str.substr(5,5*5)+str.substr((5+1)*(5+1),3);var a=encode(str.substr(4,10))+str.substr(2);var b=str.substr(6)+a.substr(2);var c=strToLong(str.substr(5))+str.substr(4);var aa=long+str.substr(4);var long=0;var a=str.substr(5);for(var i=0;i<a.length;i++){long+=(a.charCodeAt(i)<<(i%16))+i}a=long+""+str.substr(4);return hex_md5(b).substr(2,24)}function makeKey_126(str){return hex_md5(makeKey_7(str)+makeKey_1(str)).substr(3,24)}function makeKey_127(str){return hex_md5(makeKey_3(str)+makeKey_4(str)).substr(4,24)}function makeKey_128(str){return hex_md5(makeKey_7(str)+makeKey_5(str)).substr(1,24)}function makeKey_129(str){return hex_md5(makeKey_8(str)+makeKey_3(str)).substr(2,24)}function makeKey_177(str){return hex_md5(makeKey_9(str)+makeKey_0(str)).substr(3,24)}function makeKey_178(str){return hex_md5(makeKey_10(str)+makeKey_1(str)).substr(4,24)}function makeKey_179(str){return hex_md5(makeKey_17(str)+makeKey_4(str)).substr(1,24)}function makeKey_180(str){return hex_md5(makeKey_18(str)+makeKey_14(str)).substr(3,24)}"""

js_strToLong="""
function strToLong(str){var long=0;for(var i=0;i<str.length;i++){long+=(str.charCodeAt(i)<<(i%16))}return long}function strToLongEn(str){var long=0;for(var i=0;i<str.length;i++){long+=(str.charCodeAt(i)<<(i%16))+i}return long}function strToLongEn2(str,step){var long=0;for(var i=0;i<str.length;i++){long+=(str.charCodeAt(i)<<(i%16))+(i*step)}return long}function strToLongEn3(str,step){var long=0;for(var i=0;i<str.length;i++){long+=(str.charCodeAt(i)<<(i%16))+(i+step-str.charCodeAt(i))}return long}
"""

base_64="""   
       var keyStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
    function encode(input) {
        var output = '';
        var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
        var i = 0;
        input = utf8_encode(input);
        while (i < input.length) {
            chr1 = input.charCodeAt(i++);
            chr2 = input.charCodeAt(i++);
            chr3 = input.charCodeAt(i++);
            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;
            if (isNaN(chr2)) {
                enc3 = enc4 = 64;
            } else if (isNaN(chr3)) {
                enc4 = 64;
            }
            output = output +
            keyStr.charAt(enc1) + keyStr.charAt(enc2) +
            keyStr.charAt(enc3) + keyStr.charAt(enc4);
        }
        return output;
    }

    function utf8_encode(string) {
        string = string.replace(/\\r\\n/g,'\\n');
        var utftext = '';
        for (var n = 0; n < string.length; n++) {
            var c = string.charCodeAt(n);
            if (c < 128) {
                utftext += String.fromCharCode(c);
            } else if((c > 127) && (c < 2048)) {
                utftext += String.fromCharCode((c >> 6) | 192);
                utftext += String.fromCharCode((c & 63) | 128);
            } else {
                utftext += String.fromCharCode((c >> 12) | 224);
                utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                utftext += String.fromCharCode((c & 63) | 128);
            }
        }
        return utftext;
    }


"""

sha1="""
/*   
 *   A   JavaScript   implementation   of   the   Secure   Hash   Algorithm,   SHA-1,   as   defined   
 *   in   FIPS   PUB   180-1   
 *   Version   2.1-BETA   Copyright   Paul   Johnston   2000   -   2002.   
 *   Other   contributors:   Greg   Holt,   Andrew   Kepert,   Ydnar,   Lostinet   
 *   Distributed   under   the   BSD   License   
 *   See   http://pajhome.org.uk/crypt/md5   for   details.   
 */
/*   
 *   Configurable   variables.   You   may   need   to   tweak   these   to   be   compatible   with   
 *   the   server-side,   but   the   defaults   work   in   most   cases.   
 */
var hexcase = 0; /*   hex   output   format.   0   -   lowercase;   1   -   uppercase                 */
var b64pad = ""; /*   base-64   pad   character.   "="   for   strict   RFC   compliance       */
var chrsz = 8; /*   bits   per   input   character.   8   -   ASCII;   16   -   Unicode             */

/*   
 *   These   are   the   functions   you'll   usually   want   to   call   
 *   They   take   string   arguments   and   return   either   hex   or   base-64   encoded   strings   
 */
function hex_sha1(s) {
    return binb2hex(core_sha1(str2binb(s), s.length * chrsz));
}

function b64_sha1(s) {
    return binb2b64(core_sha1(str2binb(s), s.length * chrsz));
}

function str_sha1(s) {
    return binb2str(core_sha1(str2binb(s), s.length * chrsz));
}

function hex_hmac_sha1(key, data) {
    return binb2hex(core_hmac_sha1(key, data));
}

function b64_hmac_sha1(key, data) {
    return binb2b64(core_hmac_sha1(key, data));
}

function str_hmac_sha1(key, data) {
    return binb2str(core_hmac_sha1(key, data));
}

/*   
 *   Perform   a   simple   self-test   to   see   if   the   VM   is   working   
 */
function sha1_vm_test() {
    return hex_sha1("abc") == "a9993e364706816aba3e25717850c26c9cd0d89d";
}

/*   
 *   Calculate   the   SHA-1   of   an   array   of   big-endian   words,   and   a   bit   length   
 */
function core_sha1(x, len) {
    /*   append   padding   */
    x[len >> 5] |= 0x80 << (24 - len % 32);
    x[((len + 64 >> 9) << 4) + 15] = len;

    var w = Array(80);
    var a = 1732584193;
    var b = -271733879;
    var c = -1732584194;
    var d = 271733878;
    var e = -1009589776;

    for (var i = 0; i < x.length; i += 16) {
        var olda = a;
        var oldb = b;
        var oldc = c;
        var oldd = d;
        var olde = e;

        for (var j = 0; j < 80; j++) {
            if (j < 16) w[j] = x[i + j];
            else w[j] = rol(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1);
            var t = safe_add(safe_add(rol(a, 5), sha1_ft(j, b, c, d)), safe_add(safe_add(e, w[j]), sha1_kt(j)));
            e = d;
            d = c;
            c = rol(b, 30);
            b = a;
            a = t;
        }

        a = safe_add(a, olda);
        b = safe_add(b, oldb);
        c = safe_add(c, oldc);
        d = safe_add(d, oldd);
        e = safe_add(e, olde);
    }
    return Array(a, b, c, d, e);

}

/*   
 *   Perform   the   appropriate   triplet   combination   function   for   the   current   
 *   iteration   
 */
function sha1_ft(t, b, c, d) {
    if (t < 20) return (b & c) | ((~b) & d);
    if (t < 40) return b ^ c ^ d;
    if (t < 60) return (b & c) | (b & d) | (c & d);
    return b ^ c ^ d;
}

/*   
 *   Determine   the   appropriate   additive   constant   for   the   current   iteration   
 */
function sha1_kt(t) {
    return (t < 20) ? 1518500249 : (t < 40) ? 1859775393 : (t < 60) ? -1894007588 : -899497514;
}

/*   
 *   Calculate   the   HMAC-SHA1   of   a   key   and   some   data   
 */
function core_hmac_sha1(key, data) {
    var bkey = str2binb(key);
    if (bkey.length > 16) bkey = core_sha1(bkey, key.length * chrsz);

    var ipad = Array(16),
        opad = Array(16);
    for (var i = 0; i < 16; i++) {
        ipad[i] = bkey[i] ^ 0x36363636;
        opad[i] = bkey[i] ^ 0x5C5C5C5C;
    }

    var hash = core_sha1(ipad.concat(str2binb(data)), 512 + data.length * chrsz);
    return core_sha1(opad.concat(hash), 512 + 160);
}

/*   
 *   Add   integers,   wrapping   at   2^32.   This   uses   16-bit   operations   internally   
 *   to   work   around   bugs   in   some   JS   interpreters.   
 */
function safe_add(x, y) {
    var lsw = (x & 0xFFFF) + (y & 0xFFFF);
    var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
    return (msw << 16) | (lsw & 0xFFFF);
}

/*   
 *   Bitwise   rotate   a   32-bit   number   to   the   left.   
 */
function rol(num, cnt) {
    return (num << cnt) | (num >>> (32 - cnt));
}

/*   
 *   Convert   an   8-bit   or   16-bit   string   to   an   array   of   big-endian   words   
 *   In   8-bit   function,   characters   >255   have   their   hi-byte   silently   ignored.   
 */
function str2binb(str) {
    var bin = Array();
    var mask = (1 << chrsz) - 1;
    for (var i = 0; i < str.length * chrsz; i += chrsz)
    bin[i >> 5] |= (str.charCodeAt(i / chrsz) & mask) << (24 - i % 32);
    return bin;
}

/*   
 *   Convert   an   array   of   big-endian   words   to   a   string   
 */
function binb2str(bin) {
    var str = "";
    var mask = (1 << chrsz) - 1;
    for (var i = 0; i < bin.length * 32; i += chrsz)
    str += String.fromCharCode((bin[i >> 5] >>> (24 - i % 32)) & mask);
    return str;
}

/*   
 *   Convert   an   array   of   big-endian   words   to   a   hex   string.   
 */
function binb2hex(binarray) {
    var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
    var str = "";
    for (var i = 0; i < binarray.length * 4; i++) {
        str += hex_tab.charAt((binarray[i >> 2] >> ((3 - i % 4) * 8 + 4)) & 0xF) + hex_tab.charAt((binarray[i >> 2] >> ((3 - i % 4) * 8)) & 0xF);
    }
    return str;
}

/*   
 *   Convert   an   array   of   big-endian   words   to   a   base-64   string   
 */
function binb2b64(binarray) {
    var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var str = "";
    for (var i = 0; i < binarray.length * 4; i += 3) {
        var triplet = (((binarray[i >> 2] >> 8 * (3 - i % 4)) & 0xFF) << 16) | (((binarray[i + 1 >> 2] >> 8 * (3 - (i + 1) % 4)) & 0xFF) << 8) | ((binarray[i + 2 >> 2] >> 8 * (3 - (i + 2) % 4)) & 0xFF);
        for (var j = 0; j < 4; j++) {
            if (i * 8 + j * 6 > binarray.length * 32) str += b64pad;
            else str += tab.charAt((triplet >> 6 * (3 - j)) & 0x3F);
        }
    }
    return str;
}
"""

md5="""

var hexcase = 0;  /* hex output format. 0 - lowercase; 1 - uppercase        */
var b64pad  = ""; /* base-64 pad character. "=" for strict RFC compliance   */
var chrsz   = 8;  /* bits per input character. 8 - ASCII; 16 - Unicode      */


function hex_md5(s){ return binl2hex(core_md5(str2binl(s), s.length * chrsz));}
function b64_md5(s){ return binl2b64(core_md5(str2binl(s), s.length * chrsz));}
function str_md5(s){ return binl2str(core_md5(str2binl(s), s.length * chrsz));}
function hex_hmac_md5(key, data) { return binl2hex(core_hmac_md5(key, data)); }
function b64_hmac_md5(key, data) { return binl2b64(core_hmac_md5(key, data)); }
function str_hmac_md5(key, data) { return binl2str(core_hmac_md5(key, data)); }

function md5_vm_test()
{
  return hex_md5("abc") == "900150983cd24fb0d6963f7d28e17f72";
}


function core_md5(x, len)
{
  /* append padding */
  x[len >> 5] |= 0x80 << ((len) % 32);
  x[(((len + 64) >>> 9) << 4) + 14] = len;

  var a =  1732584193;
  var b = -271733879;
  var c = -1732584194;
  var d =  271733878;

  for(var i = 0; i < x.length; i += 16)
  {
    var olda = a;
    var oldb = b;
    var oldc = c;
    var oldd = d;

    a = md5_ff(a, b, c, d, x[i+ 0], 7 , -680876936);
    d = md5_ff(d, a, b, c, x[i+ 1], 12, -389564586);
    c = md5_ff(c, d, a, b, x[i+ 2], 17,  606105819);
    b = md5_ff(b, c, d, a, x[i+ 3], 22, -1044525330);
    a = md5_ff(a, b, c, d, x[i+ 4], 7 , -176418897);
    d = md5_ff(d, a, b, c, x[i+ 5], 12,  1200080426);
    c = md5_ff(c, d, a, b, x[i+ 6], 17, -1473231341);
    b = md5_ff(b, c, d, a, x[i+ 7], 22, -45705983);
    a = md5_ff(a, b, c, d, x[i+ 8], 7 ,  1770035416);
    d = md5_ff(d, a, b, c, x[i+ 9], 12, -1958414417);
    c = md5_ff(c, d, a, b, x[i+10], 17, -42063);
    b = md5_ff(b, c, d, a, x[i+11], 22, -1990404162);
    a = md5_ff(a, b, c, d, x[i+12], 7 ,  1804603682);
    d = md5_ff(d, a, b, c, x[i+13], 12, -40341101);
    c = md5_ff(c, d, a, b, x[i+14], 17, -1502002290);
    b = md5_ff(b, c, d, a, x[i+15], 22,  1236535329);

    a = md5_gg(a, b, c, d, x[i+ 1], 5 , -165796510);
    d = md5_gg(d, a, b, c, x[i+ 6], 9 , -1069501632);
    c = md5_gg(c, d, a, b, x[i+11], 14,  643717713);
    b = md5_gg(b, c, d, a, x[i+ 0], 20, -373897302);
    a = md5_gg(a, b, c, d, x[i+ 5], 5 , -701558691);
    d = md5_gg(d, a, b, c, x[i+10], 9 ,  38016083);
    c = md5_gg(c, d, a, b, x[i+15], 14, -660478335);
    b = md5_gg(b, c, d, a, x[i+ 4], 20, -405537848);
    a = md5_gg(a, b, c, d, x[i+ 9], 5 ,  568446438);
    d = md5_gg(d, a, b, c, x[i+14], 9 , -1019803690);
    c = md5_gg(c, d, a, b, x[i+ 3], 14, -187363961);
    b = md5_gg(b, c, d, a, x[i+ 8], 20,  1163531501);
    a = md5_gg(a, b, c, d, x[i+13], 5 , -1444681467);
    d = md5_gg(d, a, b, c, x[i+ 2], 9 , -51403784);
    c = md5_gg(c, d, a, b, x[i+ 7], 14,  1735328473);
    b = md5_gg(b, c, d, a, x[i+12], 20, -1926607734);

    a = md5_hh(a, b, c, d, x[i+ 5], 4 , -378558);
    d = md5_hh(d, a, b, c, x[i+ 8], 11, -2022574463);
    c = md5_hh(c, d, a, b, x[i+11], 16,  1839030562);
    b = md5_hh(b, c, d, a, x[i+14], 23, -35309556);
    a = md5_hh(a, b, c, d, x[i+ 1], 4 , -1530992060);
    d = md5_hh(d, a, b, c, x[i+ 4], 11,  1272893353);
    c = md5_hh(c, d, a, b, x[i+ 7], 16, -155497632);
    b = md5_hh(b, c, d, a, x[i+10], 23, -1094730640);
    a = md5_hh(a, b, c, d, x[i+13], 4 ,  681279174);
    d = md5_hh(d, a, b, c, x[i+ 0], 11, -358537222);
    c = md5_hh(c, d, a, b, x[i+ 3], 16, -722521979);
    b = md5_hh(b, c, d, a, x[i+ 6], 23,  76029189);
    a = md5_hh(a, b, c, d, x[i+ 9], 4 , -640364487);
    d = md5_hh(d, a, b, c, x[i+12], 11, -421815835);
    c = md5_hh(c, d, a, b, x[i+15], 16,  530742520);
    b = md5_hh(b, c, d, a, x[i+ 2], 23, -995338651);

    a = md5_ii(a, b, c, d, x[i+ 0], 6 , -198630844);
    d = md5_ii(d, a, b, c, x[i+ 7], 10,  1126891415);
    c = md5_ii(c, d, a, b, x[i+14], 15, -1416354905);
    b = md5_ii(b, c, d, a, x[i+ 5], 21, -57434055);
    a = md5_ii(a, b, c, d, x[i+12], 6 ,  1700485571);
    d = md5_ii(d, a, b, c, x[i+ 3], 10, -1894986606);
    c = md5_ii(c, d, a, b, x[i+10], 15, -1051523);
    b = md5_ii(b, c, d, a, x[i+ 1], 21, -2054922799);
    a = md5_ii(a, b, c, d, x[i+ 8], 6 ,  1873313359);
    d = md5_ii(d, a, b, c, x[i+15], 10, -30611744);
    c = md5_ii(c, d, a, b, x[i+ 6], 15, -1560198380);
    b = md5_ii(b, c, d, a, x[i+13], 21,  1309151649);
    a = md5_ii(a, b, c, d, x[i+ 4], 6 , -145523070);
    d = md5_ii(d, a, b, c, x[i+11], 10, -1120210379);
    c = md5_ii(c, d, a, b, x[i+ 2], 15,  718787259);
    b = md5_ii(b, c, d, a, x[i+ 9], 21, -343485551);

    a = safe_add(a, olda);
    b = safe_add(b, oldb);
    c = safe_add(c, oldc);
    d = safe_add(d, oldd);
  }
  return Array(a, b, c, d);

}

/*
 * These functions implement the four basic operations the algorithm uses.
 */
function md5_cmn(q, a, b, x, s, t)
{
  return safe_add(bit_rol(safe_add(safe_add(a, q), safe_add(x, t)), s),b);
}
function md5_ff(a, b, c, d, x, s, t)
{
  return md5_cmn((b & c) | ((~b) & d), a, b, x, s, t);
}
function md5_gg(a, b, c, d, x, s, t)
{
  return md5_cmn((b & d) | (c & (~d)), a, b, x, s, t);
}
function md5_hh(a, b, c, d, x, s, t)
{
  return md5_cmn(b ^ c ^ d, a, b, x, s, t);
}
function md5_ii(a, b, c, d, x, s, t)
{
  return md5_cmn(c ^ (b | (~d)), a, b, x, s, t);
}

function core_hmac_md5(key, data)
{
  var bkey = str2binl(key);
  if(bkey.length > 16) bkey = core_md5(bkey, key.length * chrsz);

  var ipad = Array(16), opad = Array(16);
  for(var i = 0; i < 16; i++)
  {
    ipad[i] = bkey[i] ^ 0x36363636;
    opad[i] = bkey[i] ^ 0x5C5C5C5C;
  }

  var hash = core_md5(ipad.concat(str2binl(data)), 512 + data.length * chrsz);
  return core_md5(opad.concat(hash), 512 + 128);
}


function safe_add(x, y)
{
  var lsw = (x & 0xFFFF) + (y & 0xFFFF);
  var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
  return (msw << 16) | (lsw & 0xFFFF);
}


function bit_rol(num, cnt)
{
  return (num << cnt) | (num >>> (32 - cnt));
}


function str2binl(str)
{
  var bin = Array();
  var mask = (1 << chrsz) - 1;
  for(var i = 0; i < str.length * chrsz; i += chrsz)
    bin[i>>5] |= (str.charCodeAt(i / chrsz) & mask) << (i%32);
  return bin;
}


function binl2str(bin)
{
  var str = "";
  var mask = (1 << chrsz) - 1;
  for(var i = 0; i < bin.length * 32; i += chrsz)
    str += String.fromCharCode((bin[i>>5] >>> (i % 32)) & mask);
  return str;
}

function binl2hex(binarray)
{
  var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
  var str = "";
  for(var i = 0; i < binarray.length * 4; i++)
  {
    str += hex_tab.charAt((binarray[i>>2] >> ((i%4)*8+4)) & 0xF) +
           hex_tab.charAt((binarray[i>>2] >> ((i%4)*8  )) & 0xF);
  }
  return str;
}


function binl2b64(binarray)
{
  var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  var str = "";
  for(var i = 0; i < binarray.length * 4; i += 3)
  {
    var triplet = (((binarray[i   >> 2] >> 8 * ( i   %4)) & 0xFF) << 16)
                | (((binarray[i+1 >> 2] >> 8 * ((i+1)%4)) & 0xFF) << 8 )
                |  ((binarray[i+2 >> 2] >> 8 * ((i+2)%4)) & 0xFF);
    for(var j = 0; j < 4; j++)
    {
      if(i * 8 + j * 6 > binarray.length * 32) str += b64pad;
      else str += tab.charAt((triplet >> 6*(3-j)) & 0x3F);
    }
  }
  return str;
}

"""