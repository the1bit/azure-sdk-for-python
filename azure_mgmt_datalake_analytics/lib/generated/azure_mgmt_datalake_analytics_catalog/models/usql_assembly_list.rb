# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::DataLakeAnalytics::Catalog
  module Models
    #
    # A Data Lake Analytics catalog U-SQL assembly CLR item list.
    #
    class USqlAssemblyList < CatalogItemList

      include MsRestAzure

      # @return [Array<USqlAssemblyClr>] the list of assemblies in the database
      attr_accessor :value

      # return [Proc] with next page method call.
      attr_accessor :next_method

      #
      # Gets the rest of the items for the request, enabling auto-pagination.
      #
      # @return [Array<USqlAssemblyClr>] operation results.
      #
      def get_all_items
        items = @value
        page = self
        while page.next_link != nil do
          page = page.get_next_page
          items.concat(page.value)
        end
        items
      end

      #
      # Gets the next page of results.
      #
      # @return [USqlAssemblyList] with next page content.
      #
      def get_next_page
        response = @next_method.call(@next_link).value! unless @next_method.nil?
        unless response.nil?
          @next_link = response.body.next_link
          @value = response.body.value
          self
        end
      end

      #
      # Mapper for USqlAssemblyList class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'USqlAssemblyList',
          type: {
            name: 'Composite',
            class_name: 'USqlAssemblyList',
            model_properties: {
              count: {
                required: false,
                serialized_name: 'count',
                type: {
                  name: 'Number'
                }
              },
              next_link: {
                required: false,
                serialized_name: 'nextLink',
                type: {
                  name: 'String'
                }
              },
              value: {
                required: false,
                read_only: true,
                serialized_name: 'value',
                type: {
                  name: 'Sequence',
                  element: {
                      required: false,
                      serialized_name: 'USqlAssemblyClrElementType',
                      type: {
                        name: 'Composite',
                        class_name: 'USqlAssemblyClr'
                      }
                  }
                }
              }
            }
          }
        }
      end
    end
  end
end