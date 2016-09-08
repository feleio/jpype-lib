import jpype
import pprint

# start the JVM with the good classpaths
jvmpath = '/Library/Java/JavaVirtualMachines/jdk1.8.0_101.jdk/Contents/Home/jre/lib/jli/libjli.dylib'
classpath = "target/lang-gen-lib-1.0-SNAPSHOT.jar:lib/SimpleNLG-4.4.9-SNAPSHOT.jar"

jpype.startJVM(jvmpath,"-ea", "-Djava.class.path=%s" % classpath)
SimplenlgWrapper = jpype.JClass("com.babylonhealth.app.SimplenlgWrapper")
print SimplenlgWrapper.run()

jpype.shutdownJVM()