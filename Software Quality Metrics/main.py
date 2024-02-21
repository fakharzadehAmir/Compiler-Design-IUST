from antlr4 import *
from Gen.Java8Parser import Java8Parser
from Gen.Java8Lexer import Java8Lexer
from ejiogu_metric import EjioguMetricsListener
from halstead_metric import HalsteadMetricListener
from readability_metric import ReadabilityMetricListener


def main():
    file_name = input("Enter Java file name: ")
    input_stream = FileStream(file_name)

    lexer = Java8Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Java8Parser(stream)

    tree = parser.compilationUnit()

    walker = ParseTreeWalker()

    eji_listener = EjioguMetricsListener()
    walker.walk(eji_listener, tree)

    print("Ejiogu's Metrics:")
    print("Structural Complexity:", eji_listener.get_structural_complexity())
    print("Software Size:", eji_listener.get_software_size())

    halstead_listener = HalsteadMetricListener()
    walker.walk(halstead_listener, tree)
    print("\n\nHalstead's Metrics:")
    print("Vocabulary:", halstead_listener.get_vocabulary())
    print("Length:", halstead_listener.get_length())
    print("Volume:", halstead_listener.get_volume())
    print("Difficulty:", halstead_listener.get_difficulty())
    print("Effort:", halstead_listener.get_effort())
    print("Time to program:", halstead_listener.get_time_to_program())

    readability_listener = ReadabilityMetricListener()
    walker.walk(readability_listener, tree)
    print("\n\nReadability's Metrics:")
    print("Lines of Code:", readability_listener.get_lines_of_code())
    print("Document Pages:", readability_listener.calculate_document_pages())


if __name__ == '__main__':
    main()
